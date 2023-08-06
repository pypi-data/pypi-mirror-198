import pandas as pd
import numpy as np

#This creates a unique order of questions for every quiz. 
#Fixes/ used to fixed the following
# question numbers when random ordering on quiz is selected
# pooling errors
# used to determine "end" of questions for binary question format
#user_attempt is the data that you are attempting to transform/ modified (with answer key) question details file
#quiz answer is the answer key/question details file
def createQuizOrder(user_attempt, quiz_answer): 
    d = dict(enumerate(quiz_answer["Q Text"].unique(),1))
    reversed_d = dict([(value, key) for key, value in d.items()])
    user_attempt["newQ#"] = user_attempt["Q Text"].apply(lambda x: reversed_d.get(x))
    user_attempt['label']=user_attempt['newQ#'].astype(str)+user_attempt.groupby(['Username','Attempt #','newQ#']).\
        cumcount().add(1).astype(str)
    user_attempt['Q Text'] = user_attempt['Q Text'].apply(lambda x: str(x).replace(u'\xa0', u''))

    return user_attempt

#Read's in csvs probably can be removed in actual use since read_csv does it already. 
def readincsv (attempt_details, quiz_details):
    user_details = pd.read_csv(attempt_details,sep=',')
    user_details = user_details.sort_values(by=['Q Text'])

    quiz_answer_details = pd.read_csv(quiz_details,sep=',')
    quiz_answer_details = quiz_answer_details.sort_values(by=['Q Text'])
    return user_details, quiz_answer_details

#append the "answerkey" to the top of the dataframe. (should be used before quiz order)
def answerKeyOnTop(attempt_details, quiz_details):
    answerkey = quiz_details.copy()
    answerkey["Attempt #"], answerkey ["Username"], answerkey ["FirstName"], answerkey["LastName"]=\
        [1, "answerKey", "Answer", "Key"]
    attempt_details = pd.concat([answerkey,attempt_details ], ignore_index=True )
    return attempt_details

#checks whether a True/False, multiple choice, or multi-select question is checked
# or not based on the 'Answer Match' Column and returns a 0 or 1.
def trufalse_mc_check(user_df, idx):
    return 1 if user_df['Answer Match'][idx] == 'Checked' else 0

#Scores True/False, multiple choice, or multi-select questions according to score value
def trufalse_mc_score(user_df, idx):
    return 0 if user_df['Score'][idx] < user_df['Out Of'][idx] else 1

#Creates a dictionary of question:question text key value pairs(For quick question lookup)
def question_dictionary(user_attempt):
    return {data["newQ#"]: (data["Q Text"]) for (index, data) in
            user_attempt[user_attempt['Username'] == 'answerKey'].iterrows()}

#Creates a dataframe with question parts
def qparts_df_creation(official):
    wide_format_df = pd.DataFrame(columns=['Org Defined ID', 'Attempt #', 'FirstName', 'LastName',
                                           'Question#', 'Answer'])
    wide_format_df.set_index('Org Defined ID', inplace=True)
    username_values = [value for value in official['Username'].unique() if value != 'answerKey']
    for username in username_values:
        for i, row in official[official['Username'] == username].iterrows():
            if official['Q Type'][i] in ['T/F', 'M-S', 'MC']:
                wide_format_df = pd.concat([wide_format_df,
                                            pd.Series({'Org Defined ID': official['Org Defined ID'][i],
                                                       'Attempt #': official['Attempt #'][i],
                                                       'FirstName': official['FirstName'][i],
                                                       'LastName': official['LastName'][i],
                                                       'Question#': official['label'][i],
                                                       'Answer': trufalse_mc_check(official, i)}).to_frame().T],
                                           ignore_index=True)
            elif official['Q Type'][i] in ['MAT', 'ORD', 'SA', 'MSA', 'FIB']:
                wide_format_df = pd.concat([wide_format_df,
                                            pd.Series({'Org Defined ID': official['Org Defined ID'][i],
                                                       'Attempt #': official['Attempt #'][i],
                                                       'FirstName': official['FirstName'][i],
                                                       'LastName': official['LastName'][i],
                                                       'Question#': official['label'][i],
                                                       'Answer': official['Answer Match'][i]}).to_frame().T],
                                           ignore_index=True)
            elif official['Q Type'][i] == 'WR':
                wide_format_df = pd.concat([wide_format_df,
                                            pd.Series({'Org Defined ID': official['Org Defined ID'][i],
                                                       'Attempt #': official['Attempt #'][i],
                                                       'FirstName': official['FirstName'][i],
                                                       'LastName': official['LastName'][i],
                                                       'Question#': official['label'][i],
                                                       'Answer': official['Answer'][i]}).to_frame().T],
                                           ignore_index=True)

    return wide_format_df[['Org Defined ID', 'Attempt #', 'FirstName', 'LastName', 'Question#', 'Answer']]

#Creates dataframe with answers for each whole question
def qwhole_df_creation(official):
    question_df = pd.DataFrame(columns=['Org Defined ID', 'Attempt #', 'FirstName', 'LastName',  'Q#', 'Answer'])
    question_df.set_index('Org Defined ID', inplace=True)
    username_values = [value for value in official['Username'].unique() if value != 'answerKey']
    for username in username_values:
        for i, row in official[official['Username'] == username].iterrows():
            if official['Q Type'][i] in ['T/F', 'M-S', 'MC']:
                question_df = pd.concat([question_df,
                                         pd.Series({'Org Defined ID': official['Org Defined ID'][i],
                                                    'Attempt #': official['Attempt #'][i],
                                                    'FirstName': official['FirstName'][i],
                                                    'LastName': official['LastName'][i],
                                                    'Q#': official['newQ#'][i],
                                                    'Answer': trufalse_mc_score(official, i)}).to_frame().T],
                                        ignore_index=True)
            elif official['Q Type'][i] in ['MAT', 'ORD', 'SA', 'MSA', 'FIB']:
                question_df = pd.concat([question_df,
                                         pd.Series({'Org Defined ID': official['Org Defined ID'][i],
                                                    'Attempt #': official['Attempt #'][i],
                                                    'FirstName': official['FirstName'][i],
                                                    'LastName': official['LastName'][i],
                                                    'Q#': official['newQ#'][i],
                                                    'Answer': official['Answer Match'][i]}).to_frame().T],
                                        ignore_index=True)
            elif official['Q Type'][i] == 'WR':
                question_df = pd.concat([question_df,
                                         pd.Series({'Org Defined ID': official['Org Defined ID'][i],
                                                    'Attempt #': official['Attempt #'][i],
                                                    'FirstName': official['FirstName'][i],
                                                    'LastName': official['LastName'][i],
                                                    'Q#': official['newQ#'][i],
                                                    'Answer': official['Answer'][i]}).to_frame().T],
                                        ignore_index=True)

    return question_df[['Org Defined ID', 'Attempt #', 'FirstName', 'LastName', 'Q#', 'Answer']]

#Returns a list of question columns for the question parts dataframe
def qparts_df_column_list_creation(new_data):
    temp_columns = []
    q_list = []

    for question in new_data['Question#']:
        if question not in q_list:
            q_list.append(question)
            temp_columns.append(str(question))
        elif question in q_list:
            q_list = []
            break

    return temp_columns

#Creates a wide binary format of the question parts dataframe
def question_parts_df_pivot(question_parts_df, col_list):
    mod_question_parts_df = pd.pivot_table(question_parts_df, index=['Org Defined ID', 'Attempt #', 'FirstName', 'LastName'],
                            values='Answer', columns=['Question#'], aggfunc='first')
    mod_question_parts_df = mod_question_parts_df.reindex(col_list, axis=1)
    mod_question_parts_df.columns = ['Q' + str(i) for i in mod_question_parts_df.columns]
    return mod_question_parts_df

#Creates a wide binary format of the question dataframe
def question_whole_df_pivot(question_whole_df):
    mod_question_df = pd.pivot_table(question_whole_df, index=['Org Defined ID', 'Attempt #', 'FirstName', 'LastName'],
                                     values='Answer', columns=['Q#'], aggfunc='first')
    mod_question_df.columns = ['Q' + str(j) for j in mod_question_df.columns]
    return mod_question_df

#uses Python's pivot_table function to convert data into a wide binary format and formats question columns
def dataframe_link(col_list, new_data, q_data):
    return pd.concat([question_parts_df_pivot(new_data, col_list), question_whole_df_pivot(q_data)], axis=1)

user_details, quiz_details = readincsv("DataFiles\Final Quiz - Attempt Details.csv", "DataFiles\Final Quiz - Question Details.csv")
mod_user_details = answerKeyOnTop(user_details, quiz_details)
mod_qorder_user_details = createQuizOrder(mod_user_details, quiz_details)
qdict = question_dictionary(mod_qorder_user_details)
question_parts_df = qparts_df_creation(mod_qorder_user_details)
question_parts_df_col_list = qparts_df_column_list_creation(question_parts_df)
question_whole_df = qwhole_df_creation(mod_qorder_user_details)
wide_format_data = dataframe_link(question_parts_df_col_list, question_parts_df, question_whole_df)
print(wide_format_data.to_string())

