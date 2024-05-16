// Collapsible
var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {

        var content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }

    });
}

let existingCustomer = false;
let questionIndex = 0;
let completedNCAnswerList = [];
let completedNCQuestionsList = [];
let NCSendBackend = false;
let intent = '';
let email = '';

let NCQuestions = [
    // personal information 
    "What should we address you as?",
    "Can we have your email address?",

    // financial objectives
    `What financial objectives are you concerned about? <br>
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Insurance', 0)">Insurance</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Savings/Investment', 1)">Savings/Investment</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Retirement', 2)">Retirement </button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Legacy Planning')">Legacy Planning </button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Full Financial Planning')">Full Financial Planning </button> <br class='button-break' />
    `,
    "Do you have any concerns with regards to your selected financial objective?",

    // schedule questions
    "Hey, let's meet up to talk more about this! Can we have your contact number?",
    `Please select an available date.
    <div class="container date-time-container">
        <input type="text" name="date" id="datepicker" class="datepicker" placeholder="Select date">
        <script>
            $(document).ready(function() {
                $(function() {
                    $(".datepicker").datepicker({
                        dateFormat: 'dd/mm/yy',
                        minDate: '0',
                        changeMonth: true,
                        changeYear: true,
                        beforeShowDay: $.datepicker.noWeekends
                    });
                });
            })
        </script>
        <input type="text" name="time" id="timepicker" class="timepicker" placeholder="Select time">
        <script type="text/javascript">
            $(document).ready(function(){
                $('.timepicker').timepicker({
                    timeFormat: 'h:mm p',
                    interval: 60,
                    minTime: '9',
                    maxTime: '6:00pm',
                    startTime: '09:00',
                    dynamic: false,
                    dropdown: true,
                    scrollbar: true
                });
            });
        </script>
        <button class=\"btn btn-danger input-button shadow\" onclick=\" getAndSendDateTime() \">Submit</button>
    </div>`,
];

let buttonlessNCQuestions = [
    "What should we address you as?",
    "Can we have your email address?",
    "What financial objectives are you concerned about?",
    "Do you have any concerns with regards to your selected financial objective?",
    "Hey, let's meet up to talk more about this! Can we have your contact number?",
    "Please select an available date.",
];

let financialObjectiveQuestions = [
    // insurance question
    `What areas of concern regarding insurance do you have? 
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Hospitalisation/Medical')">Hospitalisation/Medical</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('CareShield Life/Elder Shield')">CareShield Life/Elder Shield</button> <br class='button-break' /> 
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Early Stage/Critical Illness')">Early Stage/Critical Illness</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Death/TPD')">Death/TPD</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Personal Accident')">Personal Accident</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Home Insurance')">Home Insurance</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Travel Insurance')">Travel Insurance</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Motor Insurance')">Motor Insurance</button> <br class='button-break' />
    `,
    `What is your risk profile?
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Conservative')">Conservative</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Moderately Conservative')">Moderately Conservative</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Balanced')">Balanced</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Growth')">Growth</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Aggressive')">Aggressive</button> <br class='button-break' />
    `,
    `How many years are there left till your retirement?
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('More than 20 years')">More than 20 years</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('< 20 years')">< 20 years</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('< 10 years')">< 10 years</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('< 5 years')">< 5 years</button> <br class='button-break' />
    `,
];

let buttonlessFinancialObjectiveQuestions = [
    "What areas of concern regarding insurance do you have?",
    "What is your risk profile?",
    "How many years are there left till your retirement?",
];

// Gets the first message
function firstBotMessage() {
    $("#textInput").prop('disabled', true);
    let firstMessage = `
    Hello! Welcome to FinancialRuler. I am Candice, and I will be here to guide you through our process. 
    Before we start, are you a new customer or an existing customer? <br class='button-break'/>
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('New Customer')">New Customer</button> <br class='button-break'/>
    <button class="btn btn-danger input-button shadow" onclick="appendAndSend('Existing Customer')">Existing Customer</button>
    `;
    document.getElementById("botStarterMessage").innerHTML = '<div class="botText"><span>' + firstMessage + '</span></div>';
    document.getElementById("userInput").scrollIntoView(false);
}

//get next financial objective form question
function getNextNCQuestion() {
    //disables input box
    if (questionIndex <= 1 || questionIndex >= 3 && questionIndex < 5) { //allow name email and extra questions input
        $("#textInput").prop('disabled', false);
    } else {
        $("#textInput").prop('disabled', true);
    }

    //check for end of financial objective form
    if (questionIndex > (NCQuestions.length - 1)) {
        if (NCSendBackend != true) {
            NCSendAnswersBackend();
        }
        appendBotHtml("Thanks for letting us know your financial objectives. Thank you for your time! You may now exit this page.");
    } else {
        appendBotHtml(NCQuestions[questionIndex]);
        questionIndex += 1;
    }
}

//get extra financial objective question in a separate list
function getExtraObjectiveQuestion(index) {
    appendBotHtml(financialObjectiveQuestions[index]);
    completedNCQuestionsList.push(buttonlessFinancialObjectiveQuestions[index]);
}

// create user chat bubble and get next question/response
function appendAndSend(inputText, extraObjectiveQuestionIndex = -1) {
    removeInputs();
    //don't put appendUserHtml here else ExCust will be repeated if user wants to ask other qns

    if (inputText == "Existing Customer") {
        $("#textInput").prop('disabled', false);
        existingCustomer = true;

        if (questionIndex == 5) {
            questionIndex = 1; //to loop if user wants to ask qns again
            getNextECQuestion(inputText);
        }
        else {
            appendUserHtml(inputText);
            getNextECQuestion(inputText);
        }

    }
    else if (existingCustomer == true) {
        if (questionIndex == 3 && inputText == "Yes") {
            appendUserHtml(inputText);
            questionIndex += 1;
            getNextECQuestion(inputText);
        }
        else {
            appendUserHtml(inputText);
            getNextECQuestion(inputText);
        }
    }
    else if (extraObjectiveQuestionIndex != -1) { // to ask extra financial objective question when applicable
        appendUserHtml(inputText);
        completedNCAnswerList.push(inputText);
        getExtraObjectiveQuestion(extraObjectiveQuestionIndex);
    }
    else { //new user
        existingCustomer = false;
        getResponse(inputText);
    }
}


//create bot chat bubble
function appendBotHtml(inputText) {
    let botHtml = "";
    botHtml += '<div class="botText"><span>' + inputText.toString() + '</span></div>';
    $("#chatbox").append(botHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

// create user chat bubble
function appendUserHtml(inputText) {
    let userHtml = '<div class="userText"><span>' + inputText.toString() + '</span></div>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

async function NCSendAnswersBackend() {
    completedNCAnswerList.shift(); //remove new customer answer
    let currentUserEmail = completedNCAnswerList[1];
    for (let i = 0; i < completedNCQuestionsList.length - 1; i++) {
        try {
            await axios.post(`http://127.0.0.1:6543/addKYCUserChatReply?email=${currentUserEmail}&chatbotQuestion=${completedNCQuestionsList[i]}&userReply=${completedNCAnswerList[i]}`);
        } catch (error) {
            console.log(error);
        }
    }
    NCSendBackend = true;
}

function inputValidation(inputText) {
    if (questionIndex == 2) { //email
        if (!validateEmail(inputText)) {
            let errorHtml = "Sorry, you have entered an invalid email. Please try again.";
            appendBotHtml(errorHtml);
            questionIndex -= 1;
            completedNCQuestionsList.pop();
            completedNCAnswerList.pop();
        }
    }
    else if (questionIndex == 5) {
        if (!validatePhoneNumber(inputText)) {
            let errorHtml = "Sorry, you have entered an invalid phone number. Please try again.";
            appendBotHtml(errorHtml);
            questionIndex -= 1;
            completedNCQuestionsList.pop();
            completedNCAnswerList.pop();
        }
    }
    else if (questionIndex == 6) {
        if (!validateDateTime(inputText)) {
            let errorHtml = "Please try again.";
            appendBotHtml(errorHtml);
            questionIndex -= 1;
            completedNCQuestionsList.pop();
            completedNCAnswerList.pop();
        }
    }
    return;
}

//function for email validation with regex
function validateEmail(inputText) {
    return /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/.test(inputText);
}

function validatePhoneNumber(inputText) {
    return /^[6|8|9]\d{7}$|^\+65[6|8|9]\d{7}$|^\+65\s[6|8|9]\d{7}$/.test(inputText);
}

function validateDateTime(inputText) {
    return /^([1-9]|([012][0-9])|(3[01]))\/([0]{0,1}[1-9]|1[012])\/\d\d\d\d\s([0-1]?[0-9]|2?[0-3]):([0-5]\d)\s\w{2}$/.test(inputText);
}

// function to remove input buttons when user has selected an input button
function removeInputs() {
    $(".input-button").remove();
    $(".button-break").remove();
    $(".date-time-container").remove();
}

firstBotMessage();


//Gets the text from the input box and processes it
function getResponse(userText) {
    removeInputs();
    appendUserHtml(userText);
    if (existingCustomer == true) {
        getNextECQuestion(userText);
    } else {
        completedNCQuestionsList.push(buttonlessNCQuestions[questionIndex]);
        completedNCAnswerList.push(userText);
        inputValidation(userText);
        getNextNCQuestion();
    }
}

//send button on chat interface
function sendButton() {
    let userText = $("#textInput").val();
    if (userText == "") {
        return;
    }
    getResponse(userText);
}

// submit button to get & send Date & Time string for scheduling
function getAndSendDateTime() {
    let date = document.getElementById('datepicker').value;
    let time = document.getElementById('timepicker').value;
    let dateTime = date.toString() + " " + time.toString();
    removeInputs();
    appendAndSend(dateTime);
}

// Press enter to send a message
$("#textInput").keypress(function (e) {
    if (e.which == 13) {
        sendButton();
    }
});