from datasets import utils
import openpyxl

df = utils.load_from_tsfile_to_dataframe('/Users/joshuamiller/Documents/SULI 2023/mvts_transformer/src/datasets/Monash_UEA_UCR_Regression_Archive/BeijingPM25Quality/BeijingPM25Quality_TRAIN.ts', 
                                          return_separate_X_and_y=False)

print(df.head())

df[:15].to_excel('/Users/joshuamiller/Documents/SULI 2023/mvts_transformer/src/datasets/Monash_UEA_UCR_Regression_Archive/BeijingPM25Quality/BeijingPM25Quality_TRAIN.xlsx')