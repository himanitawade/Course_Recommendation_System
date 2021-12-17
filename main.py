from typing import Text
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
#from databaseconnection import getlistofcourses
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.expansionpanel import MDExpansionPanel,MDExpansionPanelTwoLine
from kivymd.uix.list import TwoLineListItem,OneLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
#from databaseconnection import getlistofavailablecourses
#from databaseconnection import getlistofregisteredcourses
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivymd.uix.toolbar import MDToolbar
#from databaseconnection import authenticateUser
#from databaseconnection import classenrollment
import pandas as pd
import neattext.functions as nfx
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from kivymd.uix.gridlayout import GridLayout




    
''' dailog = None
def ShowLoginErrorMessage(self):
    if not self.dialog:
        self.dialog = MDDialog(
            text = "Invalid Input"
        )
    self.dialog.open() '''
    


class HomePage(MDScreen):
    
    Course=ObjectProperty(None) 
    
    ##Algorithm to recommend course
    
    def recommend_course(self,title,Path):
        
        print(title)
        
        # Load our dataset
        df = pd.read_csv(Path)
        
        # Clean Text:stopwords,special charac
        df['clean_course_title'] = df['course_title'].apply(nfx.remove_stopwords)
        
        
        # Clean Text:stopwords,special charac
        df['clean_course_title'] = df['clean_course_title'].apply(nfx.remove_special_characters)
        
        # Vectorize our Text
        count_vect = CountVectorizer()
        
        cv_mat = count_vect.fit_transform(df['clean_course_title'])
        
        # Dense
        cv_mat = cv_mat.todense()
        
        #df_cv_words = pd.DataFrame(cv_mat.todense(),columns=count_vect.get_feature_names())
        
        # Cosine Similarity Matrix
        cosine_sim_mat = cosine_similarity(cv_mat)
        
        # Get Course ID/Index
        course_indices = pd.Series(df.index,index=df['course_title']).drop_duplicates()
        
        # ID for title
        idx = course_indices[title]
        # Course Indice
        # Search inside cosine_sim_mat
        scores = list(enumerate(cosine_sim_mat[idx]))
        
        # Sort Scores
        sorted_scores = sorted(scores,key=lambda x:x[1],reverse=True)
        # Recomm
        selected_course_indices = [i[0] for i in sorted_scores[1:]]
        
        selected_course_scores = [i[1] for i in sorted_scores[1:]]
        
        result = df['course_title'].iloc[selected_course_indices]
        
        rec_df = pd.DataFrame(result)
        
        rec_df['similarity_scores'] = selected_course_scores
        
        for r in rec_df:
            #recommendation_course = rec_df['course_title'].iloc[0]
        
            recommendation_course=rec_df['course_title'].values.tolist()
            
        print(recommendation_course)
            
        
        return (recommendation_course)
    
    
    
    def Userinterest(self,interest):
        
        self.Course = self.recommend_course(title=interest, Path ="/Users/himanitawade/Desktop/MS CS SEM 1/CPSC-481/Course Recommendation System/course_catalog1.csv")
        self.manager.current = "coursepage"
     

class CoursePage(MDScreen):
    
    
    def on_enter(self, *args):
        
        course= self.manager.get_screen('homepage').Course
        course = list(enumerate(course))
        print(course)
    
        data_tables = MDDataTable(
            size_hint=(0.9, 0.8),
            use_pagination=True,
            check = True,
            column_data=[('Index',dp(30)),('Course_name',dp(100))],
            row_data= course ,
        )
        self.manager.get_screen('coursepage').add_widget(data_tables)
        
        



############################## SCREEN MANAGER ##########################
class PageManager(ScreenManager):
    pass

#########################################################################

################# MAIN APP CLASS #################################


class CourseRecommendationSystem(MDApp):
   
    def __init__(self,**kwargs):
        super(CourseRecommendationSystem,self).__init__(**kwargs)
        self.root= Builder.load_file('pagescreen.kv')
        
       

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Orange"
        
       
        return self.root
    

######################################################
#run the application
##using command line call
if __name__ == '__main__':
    CourseRecommendationSystem().run()