//for existing customer prediction and response

let insuranceQuestions = [
    "What is your email?",
    "What would you like to know about your insurance?",
    `Did we answer your question? <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Yes') ">Yes</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('No') ">No</button> <br class='button-break' />
    `,
    "Please ask your question again.",
    `Do you still have another question? <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('Yes')">Yes</button> <br class='button-break' />
    <button class="btn btn-primary input-button shadow" onclick="appendAndSend('No')">No</button> <br class='button-break' />
    `
];


function getNextECQuestion(inputText) { //looping of qns done here

    if (questionIndex == 1 && inputText != "Existing Customer") { //email

        if (!validateEmail(inputText)) {
            let errorHtml = "Sorry, you have entered an invalid email. Please try again.";
            appendBotHtml(errorHtml);
            questionIndex -= 1;
        }
        else {
            email = inputText;
        }
    }

    if (questionIndex == 3 && inputText == "No") {
        $("#textInput").prop('disabled', false);
        appendBotHtml(insuranceQuestions[questionIndex]);
        questionIndex -= 1; //if qns not ans, asked to repeat qns again
    }
    else if (questionIndex == 3 && inputText == "Yes") {
        appendBotHtml(insuranceQuestions[questionIndex + 1]);
        questionIndex += 1; //if qns ans, ask if still have other qns
    }

    else if (questionIndex == 5 && inputText == 'No') {
        //check for end of user qns
        $("#textInput").prop('disabled', true);
        appendBotHtml("You have ended the chat. Goodbye.");
    }
    else if (questionIndex == 5 && inputText == 'Yes') { // if still have other  qns
        inputText = "Existing Customer";
        appendAndSend(inputText);
    }
    else {
        if (questionIndex == 2) { //predict
            appendPredictHtml(inputText);
        }
        else {
            appendBotHtml(insuranceQuestions[questionIndex]);
            questionIndex += 1;
        }

    }
}

// create response card
function appendResponseCardHtml(inputText) {
    let responseCardHtml = "";
    responseCardHtml += '<div id="carouselControl" class="carousel slide" data-ride="carousel"><div class="carousel-inner">';
    responseCardHtml += inputText.toString(); //info from db
    responseCardHtml += '</div><a class="carousel-control-prev" href="#carouselControl" role="button" data-slide="prev"> <i class="fa fa-chevron-left"></i><span class="sr-only">Previous</span></a><a class="carousel-control-next" href="#carouselControl" role="button" data-slide="next"> <i class="fa fa-chevron-right"></i><span class="sr-only">Next</span></a></div>'; //add arrows

    if (document.getElementsByClassName('carousel-inner').length >= 1) {
        $("#carouselControl").remove(); //remove previous cards else new cards can't work
    }

    $("#chatbox").append(responseCardHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

async function appendPredictHtml(inputText) {
    // https://codepen.io/fusco/pen/XbpaYv and https://jsonformatter.org/scss-to-css for loader
    let loaderDiv = '<div class="botText loader"><span></span><span></span><span></span></div>';
    $("#textInput").prop('disabled', true); //user unable to type during prediction
    $("#chatbox").append(loaderDiv);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
    try {
        await axios.post(`http://127.0.0.1:6543/predictionOfExistingCustomer?userQuestion=${inputText}&userEmail=${email}`).then(result => {

            intent = result.data['Predicted Label'];
            appendQueryHtml(intent);
            console.log(intent);
        });
    } catch (error) {
        console.log(error);
    }
}

async function appendQueryHtml(intent) {

    try {
        await axios.post(`http://127.0.0.1:6543/queryPredictionResponse?userEmail=${email}&prediction=${intent}`).then(query => {
            console.log(query.data);
            $(".loader").remove();

            let mpbtn = '';
            let mp = query.data.InsuranceMainPlansData;
            let rp = query.data.InsuranceRidersData;

            if (query.data['predictionanswer'] != undefined) { //not insurance plans details
                if (intent == 'fallback') { //if user ask gibberish qns
                    $("#textInput").prop('disabled', false);
                    appendBotHtml(query.data['predictionanswer']);
                }
                else if (intent == 'welcome') {
                    $("#textInput").prop('disabled', false);
                    appendBotHtml(query.data['predictionanswer'] + ' My name is Candice. Please ask your question.');
                }
                else { //specific claimables
                    appendBotHtml("You can claim: " + query.data['predictionanswer'] + ". You can also find the information in " + query.data['pagelocation']);
                    appendBotHtml(insuranceQuestions[questionIndex]);
                    questionIndex += 1;
                }
            }

            else if (query.data.Error != undefined) { //if no such user email/intent
                $("#textInput").prop('disabled', false);
                appendBotHtml("Hello, it seems like the associated email does not have any records with us. Please try asking a different question.");
            }

            else if (mp != undefined) { //response card

                if (Object.keys(mp).length >= 1) {

                    appendBotHtml("Below are the plans you have. You can click previous or next to see your other plans if you have more than 1 plan.");

                    for (let i = 0; i < Object.keys(mp).length; i++) {
                        for (let j = 0; j < Object.values(mp[Object.keys(mp)[i]]).length; j++) {
                            let detailslen = Object.keys(mp[Object.keys(mp)[i]]).length - 1;
                            if (j == 0 && i == 0) { //first card, first info
                                mpbtn += '<div class="carousel-item mySlides active"> <span><div class="myHeader"><h5 class="card-title">Insurance Main Plans</h5></div><b>' + Object.keys(mp[Object.keys(mp)[i]])[j] + ':</b> ' + Object.values(mp[Object.keys(mp)[i]])[j] + '<br>';
                            }
                            else if (j == 0) { //first info, not first card
                                mpbtn += '<div class="carousel-item mySlides"> <span><div class="myHeader"><h5 class="card-title">Insurance Main Plans</h5></div><b>' + Object.keys(mp[Object.keys(mp)[i]])[j] + ':</b> ' + Object.values(mp[Object.keys(mp)[i]])[j] + '<br>';
                            }
                            else if (j % detailslen == 0 && j != 0) { //last info in card
                                mpbtn += '<b>' + Object.keys(mp[Object.keys(mp)[i]])[j] + ':</b> ' + Object.values(mp[Object.keys(mp)[i]])[j] + '</span></div>';
                            }
                            else { //info in between a card
                                mpbtn += '<b>' + Object.keys(mp[Object.keys(mp)[i]])[j] + ':</b> ' + Object.values(mp[Object.keys(mp)[i]])[j] + '<br>';
                            }

                        }

                    }

                    if (rp != undefined) { //riders plans
                        for (let m = 0; m < Object.keys(rp).length; m++) {
                            for (let n = 0; n < Object.values(rp[Object.keys(rp)[m]]).length; n++) {
                                let rdetailslen = Object.keys(rp[Object.keys(rp)[m]]).length - 1;
                                
                                if (n == 0) { //first info, not first card
                                    mpbtn += '<div class="carousel-item mySlides"> <span><div class="myHeader"><h5 class="card-title">Insurance Rider Plans</h5></div><b>' + Object.keys(rp[Object.keys(rp)[m]])[n] + ':</b> ' + Object.values(rp[Object.keys(rp)[m]])[n] + '<br>';
                                }
                                else if (n % rdetailslen == 0 && n != 0) { //last info in card
                                    mpbtn += '<b>' + Object.keys(rp[Object.keys(rp)[m]])[n] + ':</b> ' + Object.values(rp[Object.keys(rp)[m]])[n] + '</span></div>';
                                }
                                else { //info in between a card
                                    mpbtn += '<b>' + Object.keys(rp[Object.keys(rp)[m]])[n] + ':</b> ' + Object.values(rp[Object.keys(rp)[m]])[n] + '<br>';
                                }
    
                            }
    
                        }
                    }
                    appendResponseCardHtml(mpbtn); //add card
                    appendBotHtml(insuranceQuestions[questionIndex]);
                    document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    questionIndex += 1;
                }
                else {
                    appendBotHtml(query);
                    // ask did we ans your qns
                    appendBotHtml(insuranceQuestions[questionIndex]);
                    document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    questionIndex += 1;

                }
            }
            else {
                appendBotHtml(query);
                // ask did we ans your qns
                appendBotHtml(insuranceQuestions[questionIndex]);
                document.getElementById("chat-bar-bottom").scrollIntoView(true);
                questionIndex += 1;
            }

        });
    } catch (error) {
        console.log(error);
    }
}
