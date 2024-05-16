from distutils.log import error
from pyramid.view import view_config
from pyramid.response import Response
from soupsieve import select
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import distinct
from sqlalchemy import asc
from sqlalchemy import select

import io
import sys
import json
import os
import pandas as pd
import numpy as np

from transformers import AutoTokenizer
from sklearn.preprocessing import LabelEncoder
import torch
from transformers import TrainingArguments
from sklearn.model_selection import train_test_split
from transformers import Trainer

from sqlalchemy.sql.expression import asc

#from fyp_3a62.models import 
from .. import models
from fyp_3a62.models import gf_user
from fyp_3a62.models import gf_insurance_main_plans
from fyp_3a62.models import gf_insurance_main_cash_plans
from fyp_3a62.models import gf_insurance_main_plans_payout
from fyp_3a62.models import gf_insurance_premiums_schedule
from fyp_3a62.models import gf_insurance_riders
from fyp_3a62.models import gf_insurance_riders_premium_schedule
from fyp_3a62.models import kyc_collection_table
from fyp_3a62.models import prediction_response_table
from fyp_3a62.models import aipredictionhistorytable

#render the the jinja2 template
@view_config(route_name='home', renderer='fyp_3a62:templates/chatpopup.jinja2')
def home(request):
    try:
        return {'Rendered':'Chatpopup.jinja2'}

    except SQLAlchemyError:

        return {'Error'}

@view_config(route_name='test', renderer='json')
def test(request):
        print(request)
        return {'test':'hello world'}


#Uploading of gfUserRecords client csv to Cloud Database
@view_config(route_name='addUsersRecords', renderer='json')
def addUserRecordsDB(request):
    try:
        
        #read csv file at the static/clientFolder using pandas
        gf_user_data = pd.read_csv('fyp_3a62/static/clientFolder/gf_user.csv', sep=';')

        #for every row, insert data into the table
        for index, row in gf_user_data.iterrows():

            request.dbsession.add(gf_user.gfUser(
                    mongodb_id = row['id'],
                    fullname = row['fullname'],
                    prefname = row['pref name'],
                    nationality = row['nationality'],
                    phone = row['phone'],
                    email = row['email'],
                    residenceaddress = row['residence address'],
                    residencecity = row['residence city'],
                    residencestate = row['residence state'],
                    residencecountry = row['residence country'],
                    residencezip = row['residence zip'],
                    citizenship = row['citizenship'],
                    nationalstatus = row['national status'],
                    company = row['company'],
                    designation = row['designation'],
                    workphone = row['work phone'],
                    workemail = row['work email'],
                    workaddress = row['work address'],
                    workcity = row['work city'],
                    workstate = row['work state'],
                    workcountry = row['work country'],
                    workzip = row['work zip']
                )
            )
            
        return {'user':'Added to records'}

    except:

        return {'Error':'Error in the addUserRecords api'}

#Uploading Insurance Main Plans Client CSV Data to cloud database
@view_config(route_name='addInsuranceMainPlansRecords', renderer='json')
def addInsuranceMainsPlansRecordsDB(request):
    try:

        #read client csv data at static/clientFolder using pandas
        gf_main_plans = pd.read_csv('fyp_3a62/static/clientFolder/gf_main_plans.csv', sep=';')

        #for every row of data from csv file, insert data to the table
        for index, row in gf_main_plans.iterrows():

            request.dbsession.add(gf_insurance_main_plans.gfInsuranceMainPlans(
                    mongodb_id = row['id'],
                    datecreated = row['date created'],
                    policyholder = row['policy holder'],
                    lifeassured = row['life assured'],
                    age = row['age'],
                    dob = row['dob'],
                    status = row['status'],
                    productname = row['product name'],
                    insurer = row['insurer'],
                    policynum = row['policy num'],
                    coverageterm = row['coverage term'],
                    policytype = row['policy type'],
                    dateincepted = row['date incepted'],
                    datematured = row['date matured'],
                    datepaymentmatured = row['date payment matured'],
                    nominationnominee = row['nomination nominee'],
                    nominationstatus = row['nomination status'],
                    paymentfrequency = row['payment frequency'],
                    paymentterm = row['payment term'],
                    paymentmode = row['payment mode'],
                    paymentamt = row['payment amt'],
                    hsdeductible = row['hs deductible'],
                    hscoinsured = row['hs co-insured'],
                    hsyearlylimit = row['hs yearly limit'],
                    gitravelmedicaloverseas = row['gi-travel medical overseas'],
                    gitravelpersonalaccident = row['gi-travel personal accident'],
                    gitravelregion = row['gi-travel region'],
                    gihomefixtures = row['gi-home fixtures'],
                    gihomecontents = row['gi-home contents'],
                    gimotorproperty = row['gi-motor property'],
                    gimotorperson = row['gi-motor person'],
                    gimotorworkshop = row['gi-motor workshop'],
                    gimotorncd = row['gi-motor ncd'],
                    longtermcare = row['long term care'],
                    death = row['death'],
                    totalpermdisability = row['total perm disability'],
                    disabilityincome = row['disability income'],
                    earlycriticalillness = row['early critical illness'],
                    criticalillness = row['critical illness'],
                    personalaccident = row['personal accident'],
                    hospitalizationbenefits = row['hospitalization benefits'],
                    remarks = row['remarks']
                )
            )

        return {'user':'Added to records'}

    except:

        return {'Error': 'Error in the Add Insurance Main Plans API'}

#uploading Insurance Main Plans Cash Value Client CSV data to Cloud Database 
@view_config(route_name='addInsuranceMainPlansCashValueRecords', renderer='json')
def addInsuranceMainsPlansCashValueRecordsDB(request):
    try:

        #Read client csv file from static/clientFolder using pandas 
        gf_main_plans_cash_value = pd.read_csv('fyp_3a62/static/clientFolder/gf_main_plans_cash_value.csv', sep=';')

        #for every csv row, insert csv data to table
        for index, row in gf_main_plans_cash_value.iterrows():

            request.dbsession.add(gf_insurance_main_cash_plans.gfInsuranceMainCashPlans(
                main_plan_id = row['main plan id'],
                datecreated = row['date as of'],
                year = row['year'],
                currentvalue = row['current value'],
                nonguaranteeamt = row['non guarantee amt'],
                loanamt = row['loan amt'],
                loaninterest = row['loan interest']
                )
            )

        return {'user':'Added to records'}

    except:

        return {'Error': 'Error in the Add Insurance Main Plans Cash Value Records API'}

#uploading Insurance Main plans payout client csv data from static/clientFolder to Cloud Database
@view_config(route_name='addInsuranceMainPlansPayoutRecords', renderer='json')
def addInsuranceMainPlansPayoutRecordsDB(request):
    try:

        #read client csv data using pandas
        gf_main_plans_cash_payout = pd.read_csv('fyp_3a62/static/clientFolder/gf_main_plans_payout.csv', sep=';')
        for index, row in gf_main_plans_cash_payout.iterrows():

            #for each client csv data row, insert csv data to table
            request.dbsession.add(gf_insurance_main_plans_payout.gfInsuranceMainPlansPayout(
                main_plan_id = row['main plan id'],
                startdate = row['start date'],
                enddate = row['end date'],
                payoutfrequency = row['payout frequency'],
                nonguaranteeamt = row['non guarantee amt'],
                guaranteeamt = row['guaranteed amt']
                )
            )
        
        return {'user': 'Added Reocrds'}

    except:

        return {'Error': 'Error in the add Insurance Main Plans Payout Records'}

#Upload Insurance Premiums Schedule Csv Data to Cloud Database
@view_config(route_name='addInsuranceMainPlansPremiumScheduleRecords', renderer='json')
def addInsuranceMainPlansPremiumScheduleRecordsDB(request):
    try:

        #read client csv data from static/clientFolder using pandas
        gf_main_plans_premium_schedule = pd.read_csv('fyp_3a62/static/clientFolder/gf_insurance_premiums_schedule.csv', sep=';')

        #for each csv client row, insert csv data to table 
        for index, row in gf_main_plans_premium_schedule.iterrows():

            request.dbsession.add(gf_insurance_premiums_schedule.gfInsuranceMainPlansPremiumSchedule(
                main_plan_id = row['main plan id'],
                year = row['year'],
                month = row['month'],
                date = row['date'],
                premiums = row['premiums'],
                paymentmode = row['payment mode']
                )
            )
        
        return {'user': 'Added Reocrds'}

    except:

        return {'Error': 'Error in the add Insurance Main Plans Premium Schedule Records API'}

#Uploading Insurance Riders csv data to cloud database
@view_config(route_name='addUInsuranceRidersRecords', renderer='json')
def addUInsuranceRidersRecordsDB(request):
    try:

        #Read client csv data from static/clientFolder
        gf_insurance_riders_data = pd.read_csv('fyp_3a62/static/clientFolder/gf_insurance_riders.csv', sep=';')
        for index, row in gf_insurance_riders_data.iterrows():

            # 
            request.dbsession.add(gf_insurance_riders.gfInsuranceRiders(
                mongodb_rider_id =row['rider_id'],
                main_plan_id =row['mainplan id'],
                ageofentry = row['age of entry'],
                productname = row['product name'],
                insurer = row['insurer'],
                policynum = row['policy num'],
                coverageterm = row['coverage term'],
                dateincepted = row['date incepted'],
                datematured = row['date matured'],
                paymentfrequency = row['payment frequency'],
                paymentterm = row['payment term'],
                paymentmode = row['payment mode'],
                paymentamt = row['payment amt'],
                longtermcare = row['long term care'],
                death = row['death'],
                totalpermdisability = row['total perm disability'],
                disabilityincome = row['disability income'],
                earlycriticalillness = row['early critical illness'],
                criticalillness = row['critical illness'],
                personalaccident = row['personal accident'],
                hospitalizationbenefits = row['hospitalization benefits'],
                remarks = row['remarks']
                )
            )
        
        return {'user': 'Added Reocrds'}

    except:

        return {'Error': 'Error in the add Insurance Riders API'}

@view_config(route_name='addInsuranceRidersPremiumsScheduleRecords', renderer='json')
def addInsuranceRidersPremiumsScheduleRecordsDB(request):
    try:
        gf_insurance_riders_premium_schedule_data = pd.read_csv('fyp_3a62/static/clientFolder/gf_insurance_riders_premium_schedule.csv', sep=';')
        for index, row in gf_insurance_riders_premium_schedule_data.iterrows():

            request.dbsession.add(gf_insurance_riders_premium_schedule.gfInsuranceRidersPremiumSchedule(
                rider_id = row['rider id'],
                main_plan_id = row['main plan id'],
                year = row['year'],
                month = row['month'],
                date = row['date'],
                premiums = row['premiums'],
                paymentmode = row['payment mode']
                )
            )
        
        return {'user': 'Added Reocrds'}

    except:

        return {'Error': 'Error in the Add Insurance Riders Premium Schedule Records'}


#Collect Responses KYC ChatHistory
@view_config(route_name='addKYCUserChatReply', renderer='json')
def addKYCUserChatReply(request):
    try:

        email = str(request.params['email'])
        chatbotQuestion = str(request.params['chatbotQuestion'])
        userReply = str(request.params['userReply'])

        #if there is a email user and questionfield there already then remove and update
        query = request.dbsession.query(kyc_collection_table.kycChatCollectionTable)
        checkDatabaseData = query.where(kyc_collection_table.kycChatCollectionTable.useremail == email).where(kyc_collection_table.kycChatCollectionTable.question == chatbotQuestion).all()

        #delete if there is already
        if checkDatabaseData:
            checkDatabaseData = query.where(kyc_collection_table.kycChatCollectionTable.useremail == email).where(kyc_collection_table.kycChatCollectionTable.question == chatbotQuestion).delete()
            
        #Add new Records to Database
        request.dbsession.add(kyc_collection_table.kycChatCollectionTable(
            useremail = str(email).strip() ,
            question = str(chatbotQuestion).strip() ,
            userreply = str(userReply).strip(),
            )
        )
        
        return {'user': 'Added Reocrds'}

    except:

        return {'Error': 'Error in the KYC Collection Table AKA financial Objective API'}

# for model prediction
class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels=None):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        if self.labels:
            item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.encodings["input_ids"])

def preparing(testq, tokenizer):
    testq_list = testq.tolist()
    test_t = tokenizer(testq_list, truncation=True, padding=True)
    return test_t

# prediction to table
@view_config(route_name='predictionOfExistingCustomer', renderer='json')
def predictionOfExistingCustomer(request):
    print(request)
    try:
        userQuestion = request.params['userQuestion']
        email = request.params['userEmail']
        print(userQuestion)

        df = pd.read_csv("../fyp_3a62/fyp_3a62/static/nlp/data.csv")

        # transform data
        labelencoder = LabelEncoder()
        labelencoder.fit(df['label'].tolist())

        # encode text
        pretrained = 'bert-base-uncased'
        tokenizer = AutoTokenizer.from_pretrained(pretrained)
        
        # #AI Model File
        torchmodel = "../fyp_3a62/fyp_3a62/static/nlp/model.pt"
        #Load from this
        ai_model = torch.load(torchmodel, map_location=torch.device('cpu'))
        
        print('Has access to GPU: ', torch.cuda.is_available())

        trainer = Trainer(
                    model=ai_model
                )

        customer = np.array([str(userQuestion)])
        qns = Dataset(preparing(customer,tokenizer))
        ans = trainer.predict(qns).predictions.argmax(1)
        result = labelencoder.inverse_transform(ans)
        print("The label is:", result[0])

        request.dbsession.add(aipredictionhistorytable.aiPredictionHistoryTable(
            userquestion = str(userQuestion).strip() ,
            predictionlabel = str(result[0]).strip(),
            user_email = str(email).strip(),
            )
        )

        #returns the prediction label to frontend
        return {'Predicted Label': result[0]}

    except:
        return {'Error' : 'Error in the Prediction API'}

#Query Response After the Prediction Label has been asked
@view_config(route_name='queryPredictionResponse', renderer='json')
def queryPredictionResponse(request):
    try:
            predictedLabel = request.params['prediction']
            userEmail = request.params['userEmail']

            print(predictedLabel, userEmail)

            if str(predictedLabel) == 'payment_freq':

                #Insurance Main Plans & Insurance Riders
                #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                insuranceRidersData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Policy Type': str(x.policytype),
                        'Date Incepted': str(x.dateincepted),
                        'Date Matured': str(x.datematured),
                        'Date Payment Matured': str(x.datepaymentmatured),
                        'Payment Frequency': str(x.paymentfrequency),
                        'Payment Term': str(x.paymentterm),
                        'Payment Mode': str(x.paymentmode),
                        'Payment Amount': str(x.paymentamt)
                    }

                    #Insurance Riders Table Data
                    #check if there is data at related tables to the first for loop
                    queryInsuranceRiders = request.dbsession.query(gf_insurance_riders.gfInsuranceRiders)
                    insuranceRidersQueryData = queryInsuranceRiders.where(gf_insurance_riders.gfInsuranceRiders.main_plan_id == x.mongodb_id).all()
                    if insuranceRidersQueryData:
                        for y in insuranceRidersQueryData:

                            insuranceRidersData[x.mongodb_id] = {
                                'Age Of Entry': str(y.ageofentry),
                                'Product Name': str(y.productname),
                                'Insurer': str(y.insurer),
                                'Policy Number': str(y.policynum),
                                'Coverage Term': str(y.coverageterm),
                                'Date Incepted': str(y.dateincepted),
                                'Payment Term': str(y.paymentterm),
                                'Payment Mode': str(y.paymentmode),
                                'Payment Amount': str(y.paymentamt)
                            }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                    'InsuranceRidersData' : insuranceRidersData
                }

            if str(predictedLabel) == 'payment_mode':
                #Insurance main Plans & Insurnace Riders

               #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                insuranceRidersData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Policy Type': str(x.policytype),
                        'Date Incepted': str(x.dateincepted),
                        'Date Matured': str(x.datematured),
                        'Date Payment Matured': str(x.datepaymentmatured),
                        'Payment Frequency': str(x.paymentfrequency),
                        'Payment Term': str(x.paymentterm),
                        'Payment Mode': str(x.paymentmode),
                        'Payment Amount': str(x.paymentamt),
                    }

                    #Insurance Riders Table Data
                    #check if there is data at related tables to the first for loop
                    queryInsuranceRiders = request.dbsession.query(gf_insurance_riders.gfInsuranceRiders)
                    insuranceRidersQueryData = queryInsuranceRiders.where(gf_insurance_riders.gfInsuranceRiders.main_plan_id == x.mongodb_id).all()
                    if insuranceRidersQueryData:
                        for y in insuranceRidersQueryData:

                            insuranceRidersData[x.mongodb_id] = {
                                'Product Name': str(y.productname),
                                'Insurer': str(y.insurer),
                                'Policy Number': str(y.policynum),
                                'Coverage Term': str(y.coverageterm),
                                'Date Incepted': str(y.dateincepted),
                                'Payment Term': str(y.paymentterm),
                                'Payment Mode': str(y.paymentmode),
                                'Payment Amount': str(y.paymentamt)
                            }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                    'InsuranceRidersData' : insuranceRidersData
                }
            
            if str(predictedLabel) == 'insurer':
                #Insurance Main Plans & Insurance Riders

                #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                insuranceRidersData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Life Assured': str(x.lifeassured),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Status': str(x.status),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Policy Type': str(x.policytype)
                    }

                    #Insurance Riders Table Data
                    #check if there is data at related tables to the first for loop
                    queryInsuranceRiders = request.dbsession.query(gf_insurance_riders.gfInsuranceRiders)
                    insuranceRidersQueryData = queryInsuranceRiders.where(gf_insurance_riders.gfInsuranceRiders.main_plan_id == x.mongodb_id).all()
                    if insuranceRidersQueryData:
                        for y in insuranceRidersQueryData:

                            insuranceRidersData[x.mongodb_id] = {
                                'Age Of Entry': str(y.ageofentry),
                                'Product Name': str(y.productname),
                                'Insurer': str(y.insurer),
                                'Policy Number': str(y.policynum),
                                'Coverage Term': str(y.coverageterm),
                                'Date Incepted': str(y.dateincepted)
                            }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                    'InsuranceRidersData' : insuranceRidersData
                }
            
            if str(predictedLabel) == 'product_name':
                #Insurance Main Plans & Insurance Riders

                #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                insuranceRidersData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Life Assured': str(x.lifeassured),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Status': str(x.status),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Policy Type': str(x.policytype)
                    }

                    #Insurance Riders Table Data
                    #check if there is data at related tables to the first for loop
                    queryInsuranceRiders = request.dbsession.query(gf_insurance_riders.gfInsuranceRiders)
                    insuranceRidersQueryData = queryInsuranceRiders.where(gf_insurance_riders.gfInsuranceRiders.main_plan_id == x.mongodb_id).all()
                    if insuranceRidersQueryData:
                        for y in insuranceRidersQueryData:

                            insuranceRidersData[x.mongodb_id] = {
                                'Age Of Entry': str(y.ageofentry),
                                'Product Name': str(y.productname),
                                'Insurer': str(y.insurer),
                                'Policy Number': str(y.policynum),
                                'Coverage Term': str(y.coverageterm),
                                'Date Incepted': str(y.dateincepted)
                            }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                    'InsuranceRidersData' : insuranceRidersData
                }
            
            if str(predictedLabel) == 'payout_freq':
                #Insurance Main Plans Payout & Insurance Main Plans

               #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                insuranceMainPlansPayoutData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Policy Type': str(x.policytype),
                        'Date Incepted': str(x.dateincepted),
                        'Date Matured': str(x.datematured),
                        'Date Payment Matured': str(x.datepaymentmatured),
                        'Payment Frequency': str(x.paymentfrequency),
                        'Payment Term': str(x.paymentterm),
                        'Payment Mode': str(x.paymentmode),
                        'Payment Amount': str(x.paymentamt)
                    }

                    #Insurance Main Plans Payout Table Data
                    #check if there is data at related tables to the first for loop
                    queryInsuranceMainPlansPayout = request.dbsession.query(gf_insurance_main_plans_payout.gfInsuranceMainPlansPayout)
                    insuranceMainPlansPayoutQueryData = queryInsuranceMainPlansPayout.where(gf_insurance_main_plans_payout.gfInsuranceMainPlansPayout.main_plan_id == x.mongodb_id).all()
                    if insuranceMainPlansPayoutQueryData:
                        for y in insuranceMainPlansPayoutQueryData:
                            insuranceMainPlansPayoutData[x.mongodb_id] = {
                                'insurance_main_plans_payout': str(y.insurance_main_plans_payout),
                                'Start Date': str(y.startdate),
                                'End Date': str(y.enddate),
                                'Payout Frequency': str(y.payoutfrequency),
                                'Non Guarantee Amount': str(y.nonguaranteeamt),
                                'Guarantee Amount': str(y.guaranteeamt)
                            }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                    'InsuranceMainPlansPayoutData' : insuranceMainPlansPayoutData
                }
            
            if str(predictedLabel) == 'coverage_term':
                #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                insuranceRidersData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Policy Type': str(x.policytype),
                        'Date Incepted': str(x.dateincepted),
                        'Date Matured': str(x.datematured),
                        'Date Payment Matured': str(x.datepaymentmatured),
                        'Payment Frequency': str(x.paymentfrequency),
                        'Payment Term': str(x.paymentterm),
                        'Payment Mode': str(x.paymentmode),
                        'Payment Amount': str(x.paymentamt)
                    }

                    #Insurance Riders Table Data
                    #check if there is data at related tables to the first for loop
                    queryInsuranceRiders = request.dbsession.query(gf_insurance_riders.gfInsuranceRiders)
                    insuranceRidersQueryData = queryInsuranceRiders.where(gf_insurance_riders.gfInsuranceRiders.main_plan_id == x.mongodb_id).all()
                    if insuranceRidersQueryData:
                        for y in insuranceRidersQueryData:

                            insuranceRidersData[x.mongodb_id] = {
                                'Age Of Entry': str(y.ageofentry),
                                'Product Name': str(y.productname),
                                'Insurer': str(y.insurer),
                                'Policy Number': str(y.policynum),
                                'Coverage Term': str(y.coverageterm),
                                'Date Incepted': str(y.dateincepted),
                                'Payment Term': str(y.paymentterm),
                                'Payment Mode': str(y.paymentmode),
                                'Payment Amount': str(y.paymentamt)
                            }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                    'InsuranceRidersData' : insuranceRidersData
                }

            if str(predictedLabel) == 'policy_type':
                #Insurance Main Plans & gf Insurance Riders

                #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                insuranceRidersData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Life Assured': str(x.lifeassured),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Status': str(x.status),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Policy Type': str(x.policytype)
                    }

                    #Insurance Riders Table Data
                    #check if there is data at related tables to the first for loop
                    queryInsuranceRiders = request.dbsession.query(gf_insurance_riders.gfInsuranceRiders)
                    insuranceRidersQueryData = queryInsuranceRiders.where(gf_insurance_riders.gfInsuranceRiders.main_plan_id == x.mongodb_id).all()
                    if insuranceRidersQueryData:
                        for y in insuranceRidersQueryData:

                            insuranceRidersData[x.mongodb_id] = {
                                'Age Of Entry': str(y.ageofentry),
                                'Product Name': str(y.productname),
                                'Insurer': str(y.insurer),
                                'Policy Number': str(y.policynum),
                                'Coverage Term': str(y.coverageterm)
                            }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                    'InsuranceRidersData' : insuranceRidersData
                }

            if str(predictedLabel) == 'life_assured':
                #Insurance Main Plans

                #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Life Assured': str(x.lifeassured),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Status': str(x.status),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Policy Type': str(x.policytype)
                    }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                }

            if str(predictedLabel) == 'payment_duration':
                #Insurance Main Plans

                #query to get policy holder name from gfUser
                queryUser = request.dbsession.query(gf_user.gfUser)
                gfUserName = queryUser.where(gf_user.gfUser.email == userEmail).one()

                #gets the user full name from gfUser to check with the gfInsuranceMainPlans policy holder
                userFullName = gfUserName.fullname

                #Insurance Main Plans Data
                query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
                insuranceMainPlansQueryData = query.where(gf_insurance_main_plans.gfInsuranceMainPlans.policyholder == userFullName).all()
                insuranceMainPlansData = {}
                for x in insuranceMainPlansQueryData:
                    insuranceMainPlansData[x.mongodb_id] = {
                        'Policy Holder': str(x.policyholder),
                        'Age': str(x.age),
                        'Date Of Birth': str(x.dob),
                        'Product Name': str(x.productname),
                        'Insurer': str(x.insurer),
                        'Policy Number': str(x.policynum),
                        'Coverage Term': str(x.coverageterm),
                        'Date Incepted': str(x.dateincepted),
                        'Date Matured': str(x.datematured),
                        'Date Payment Matured': str(x.datepaymentmatured),
                        'Payment Frequency': str(x.paymentfrequency),
                        'Payment Term': str(x.paymentterm),
                        'Payment Mode': str(x.paymentmode),
                        'Payment Amount': str(x.paymentamt)
                    }

                return {
                    'InsuranceMainPlansData' : insuranceMainPlansData,
                }

            if str(predictedLabel) == 'claimable':
                text = 'got nothing so far'
                return text

            if str(predictedLabel) != '':

                #check in response table for the cloumn for the predicted table
                #do a Query
                brochureQuery = request.dbsession.query(prediction_response_table.predictionResponseTable)
                queryBrochureResponse = brochureQuery.filter(prediction_response_table.predictionResponseTable.predictionlabel == predictedLabel).one()

                #check if there is any response data from the variable name
                #if there is........
                if queryBrochureResponse:

                    #insert response to database table history
                    return{
                        'predictionresponsetable_id' : str(queryBrochureResponse.predictionreponsetable_id),
                        'predictionlabel' : str(queryBrochureResponse.predictionlabel),
                        'predictionanswer' : str(queryBrochureResponse.predictionanswer),
                        'pagelocation' : str(queryBrochureResponse.pagelocation),
                        'dateupdated': str(queryBrochureResponse.dateupdated)
                    } 

                return {'Data': 'No Response'}
                
                #insert response to database table history


            #returns the prediction label to frontend
            return {'Data': 'No Data Found'}

    except:
            return {'Error':'Error in the Query Response From DB API'}

# Users Table Page
@view_config(route_name='users', renderer='fyp_3a62:templates/user.jinja2')
def users(request):
    try:
        return {'Rendered':'user.jinja2'}

    except:
        return {'Error' : 'There is an error at the user.jinja2 file.'}

# Get All Users to show in table
@view_config(route_name='getAllGfUser', renderer='json')
def getAllGfUser(request):
    try:
        GfUserListTableData = []

        query = request.dbsession.query(gf_user.gfUser)
        for i in query:
            datalist = {
                'user_id': str(i.user_id),
                'mongodb_id': (i.mongodb_id),
                'fullname': (i.fullname),
                'prefname': (i.prefname),
                'nationality': (i.nationality)
            }

            GfUserListTableData.append(datalist)

        return GfUserListTableData

    except:
        return {'Error' : 'There is an error.'}

# Insurance Main Plans Table Page
@view_config(route_name='main_plans', renderer='fyp_3a62:templates/insuranceMainPlans.jinja2')
def main_plans(request):
    try:
        return {'Rendered':'insuranceMainPlans.jinja2'}

    except:
        return {'Error' : 'There is an error at the insuranceMainPlans.jinja2 file.'}

# Get All Insurance Main Plans to show in table
@view_config(route_name='getAllGfMainPlans', renderer='json')
def getAllGfMainPlans(request):
    try:
        GfMainPlansListTableData = []

        query = request.dbsession.query(gf_insurance_main_plans.gfInsuranceMainPlans)
        for i in query:
            datalist = {
                'insurance_id': str(i.insurance_id),
                'mongodb_id': (i.mongodb_id),
                'dateCreated': (i.datecreated),
                'policyHolder': (i.policyholder)
            }

            GfMainPlansListTableData.append(datalist)

        return GfMainPlansListTableData

    except:
        return {'Error' : 'There is an error.'}

# Insurance Main Plans Payout Table Page
@view_config(route_name='main_plans_payout', renderer='fyp_3a62:templates/insuranceMainPlansPayout.jinja2')
def main_plans_payout(request):
    try:
        return {'Rendered':'insuranceMainPlansPayout.jinja2'}

    except:
        return {'Error' : 'There is an error at the insuranceMainPlansPayout.jinja2 file.'}

# Get All Insurance Main Plans Payout to show in table
@view_config(route_name='getAllGfMainPlansPayout', renderer='json')
def getAllGfMainPlansPayout(request):
    try:
        GfMainPlansPayoutListTableData = []

        query = request.dbsession.query(gf_insurance_main_plans_payout.gfInsuranceMainPlansPayout)
        for i in query:
            datalist = {
                'insurance_main_plans_payout': str(i.insurance_main_plans_payout),
                'main_plan_id': (i.main_plan_id),
                'startDate': (i.startdate)
            }

            GfMainPlansPayoutListTableData.append(datalist)

        return GfMainPlansPayoutListTableData

    except:
        return {'Error' : 'There is an error.'}

# Insurance Main Cash Plans Table Page
@view_config(route_name='main_cash_plans', renderer='fyp_3a62:templates/insuranceMainCashPlans.jinja2')
def main_cash_plans(request):
    try:
        return {'Rendered':'insuranceMainCashPlans.jinja2'}

    except:
        return {'Error' : 'There is an error at the insuranceMainCashPlans.jinja2 file.'}

# Get All Insurance Main Cash Plans to show in table
@view_config(route_name='getAllGfMainCashPlans', renderer='json')
def getAllGfMainCashPlans(request):
    try:
        GfMainCashPlansListTableData = []

        query = request.dbsession.query(gf_insurance_main_cash_plans.gfInsuranceMainCashPlans)
        for i in query:
            datalist = {
                'insurance_main_cash_plans_id': str(i.insurance_main_cash_plans_id),
                'main_plan_id': (i.main_plan_id),
                'dateCreated': (i.datecreated)
            }

            GfMainCashPlansListTableData.append(datalist)

        return GfMainCashPlansListTableData

    except:
        return {'Error' : 'There is an error.'}

# Insurance Main Plans Premium Table Page
@view_config(route_name='main_plans_premium', renderer='fyp_3a62:templates/insuranceMainPlansPremiumSchedule.jinja2')
def main_plans_premium(request):
    try:
        return {'Rendered':'insuranceMainPlansPremiumSchedule.jinja2'}

    except:
        return {'Error' : 'There is an error at the insuranceMainPlansPremiumSchedule.jinja2 file.'}

# Get All Insurance Main Plans Premium to show in table
@view_config(route_name='getAllGfMainPlansPremium', renderer='json')
def getAllGfMainPlansPremium(request):
    try:
        GfMainPlansPremiumListTableData = []

        query = request.dbsession.query(gf_insurance_premiums_schedule.gfInsuranceMainPlansPremiumSchedule)
        for i in query:
            datalist = {
                'insurance_main_plans_premium_schedule_id': str(i.insurance_main_plans_premium_schedule_id),
                'main_plan_id': (i.main_plan_id),
                'year': (i.year)
            }

            GfMainPlansPremiumListTableData.append(datalist)

        return GfMainPlansPremiumListTableData

    except:
        return {'Error' : 'There is an error.'}

# Insurance Riders Table Page
@view_config(route_name='riders', renderer='fyp_3a62:templates/insuranceRiders.jinja2')
def riders(request):
    try:
        return {'Rendered':'insuranceRiders.jinja2'}

    except:
        return {'Error' : 'There is an error at the insuranceRiders.jinja2 file.'}

# Get All Insurance Riders to show in table
@view_config(route_name='getAllGfRiders', renderer='json')
def getAllGfRiders(request):
    try:
        GfRidersListTableData = []

        query = request.dbsession.query(gf_insurance_riders.gfInsuranceRiders)
        for i in query:
            datalist = {
                'insurance_riders_id': str(i.insurance_riders_id),
                'mongodb_rider_id': (i.mongodb_rider_id),
                'main_plan_id': (i.main_plan_id),
                'ageOfEntry': (i.ageofentry),
                'productName': (i.productname),
                'insurer': (i.insurer),
                'policyNum': (i.policynum)
            }

            GfRidersListTableData.append(datalist)

        return GfRidersListTableData

    except:
        return {'Error' : 'There is an error.'}

# Insurance Riders Premium Table Page
@view_config(route_name='riders_premium', renderer='fyp_3a62:templates/insuranceRidersPremiumSchedule.jinja2')
def riders_premium(request):
    try:
        return {'Rendered':'insuranceRidersPremiumSchedule.jinja2'}

    except:
        return {'Error' : 'There is an error at the insuranceRidersPremiumSchedule.jinja2 file.'}

# Get All Insurance Riders Premium to show in table
@view_config(route_name='getAllGfRidersPremium', renderer='json')
def getAllGfRidersPremium(request):
    try:
        GfRidersPremiumListTableData = []

        query = request.dbsession.query(gf_insurance_riders_premium_schedule.gfInsuranceRidersPremiumSchedule)
        for i in query:
            datalist = {
                'insurance_riders_premium_schedule_id': str(i.insurance_riders_premium_schedule_id),
                'rider_id': (i.rider_id),
                'main_plan_id': (i.main_plan_id),
                'year': (i.year)
            }

            GfRidersPremiumListTableData.append(datalist)

        return GfRidersPremiumListTableData

    except:
        return {'Error' : 'There is an error.'}
