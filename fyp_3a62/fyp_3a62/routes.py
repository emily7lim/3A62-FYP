def includeme(config):

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    ################################################################
    # Dashboard

    # Display User's Records in the Dashboard
    config.add_route('users', '/users')

    # Display Insurance Main Plans Records in the Dashboard
    config.add_route('main_plans', '/main_plans')

    # Display Insurance Main Plans Payout Records in the Dashboard
    config.add_route('main_plans_payout', '/main_plans_payout')

    # Display Insurance Main Cash Plans Records in the Dashboard
    config.add_route('main_cash_plans', '/main_cash_plans')

    # Display Insurance Main Plans Premium Schedule Records in the Dashboard
    config.add_route('main_plans_premium', '/main_plans_premium')

    # Display Insurance Riders Records in the Dashboard
    config.add_route('riders', '/riders')

    # Display Insurance Riders Premium Schedule Records in the Dashboard
    config.add_route('riders_premium', '/riders_premium')

    # Get User's Records in the Dashboard
    config.add_route('getAllGfUser', '/getAllGfUser')

    # Get Insurance Main Plans Records in the Dashboard
    config.add_route('getAllGfMainPlans', '/getAllGfMainPlans')

    # Get Insurance Main Plans Payout Records in the Dashboard
    config.add_route('getAllGfMainPlansPayout', '/getAllGfMainPlansPayout')

    # Get Insurance Main Cash Plans Records in the Dashboard
    config.add_route('getAllGfMainCashPlans', '/getAllGfMainCashPlans')

    # Get Insurance Main Plans Premium Schedule Records in the Dashboard
    config.add_route('getAllGfMainPlansPremium', '/getAllGfMainPlansPremium')

    # Get Insurance Riders Records in the Dashboard
    config.add_route('getAllGfRiders', '/getAllGfRiders')

    # Get Insurance Riders Premium Schedule Records in the Dashboard
    config.add_route('getAllGfRidersPremium', '/getAllGfRidersPremium')


    ################################################################
    # Database

    config.add_route('test', '/test')

    #Add User's Records into Database
    config.add_route('addUsersRecords', '/addUsersRecordsDatabase')

    #Add Insurance Main Plans Records into Database
    config.add_route('addInsuranceMainPlansRecords', '/addInsuranceMainPlansRecordsDatabase')

    #Add Insurance Main Plans Cash Value
    config.add_route('addInsuranceMainPlansCashValueRecords', '/addInsuranceMainPlansVashValueRecordsDatabase')

    #Add Insurance Main Plans Payout
    config.add_route('addInsuranceMainPlansPayoutRecords', '/addInsuranceMainPlansPayoutRecordsDatabase')

    #Add Insurance Main Plans Premiums Schedule
    config.add_route('addInsuranceMainPlansPremiumScheduleRecords', '/addInsuranceMainPlansPremiumScheduleRecordsDatabase')

    #Add Insurance Riders
    config.add_route('addUInsuranceRidersRecords', '/addInsuranceRidersRecordsDatabase')

    #Add Insurance Riders Premiums Schedule
    config.add_route('addInsuranceRidersPremiumsScheduleRecords', '/addInsuranceRidersPremiumsScheduleRecordsDatabase')

    ################################################################ 
    # KYC - New Customer

    # render KYC Chatbot template
    config.add_route('renderKYCChatbotTemplate', '/kycChabot')

    # Collect the responses
    config.add_route('addKYCUserChatReply', '/addKYCUserChatReply')

    ################################################################
    #Login/Logout - Existing Customer

    # Render Login/Logout template

    # Check username & password and assign session token


    ################################################################
    # Chatbot - Existing Customer (Must be assigned a session token)

    # Show chat history

    ################################################################
    # Intent Classification Model - Existing Customer

    # Model Predictions
  
    config.add_route('predictionOfExistingCustomer', '/predictionOfExistingCustomer')
    
    config.add_route('queryPredictionResponse', '/queryPredictionResponse')

    ################################################################

    
    #config.add_route('home', '/')
