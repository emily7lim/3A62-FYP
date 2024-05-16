// Get All Users function to display in table
function getAllGfUser() {
    try {
        axios.get("http://127.0.0.1:6543/getAllGfUser").then(query => {
            let tableData = query.data;
            console.log(tableData);

            for (var i = 0; i < tableData.length; i++) {
                var htmlString =
                    `
                   <tr data-active="N">
                       <td>${tableData[i].user_id}</td>
                       <td>${tableData[i].mongodb_id}</td>
                       <td>${tableData[i].fullname}</td>
                       <td>${tableData[i].prefname}</td>
                       <td>${tableData[i].nationality}</td>
                   </tr>
                `;

                $('#gfUser-list-tbody').append(htmlString);
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// Get All Insurance Main Plans function to display in table
function getAllGfMainPlans() {
    try {
        axios.get("http://127.0.0.1:6543/getAllGfMainPlans").then(query => {
            let tableData = query.data;
            console.log(tableData);

            for (var i = 0; i < tableData.length; i++) {
                var htmlString =
                    `
                   <tr data-active="N">
                       <td>${tableData[i].insurance_id}</td>
                       <td>${tableData[i].mongodb_id}</td>
                       <td>${tableData[i].dateCreated}</td>
                       <td>${tableData[i].policyHolder}</td>
                   </tr>
                `;

                $('#gfInsuranceMainPlans-list-tbody').append(htmlString);
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// Get All Insurance Main Plans Payout function to display in table
function getAllGfMainPlansPayout() {
    try {
        axios.get("http://127.0.0.1:6543/getAllGfMainPlansPayout").then(query => {
            let tableData = query.data;
            console.log(tableData);

            for (var i = 0; i < tableData.length; i++) {
                var htmlString =
                    `
                   <tr data-active="N">
                       <td>${tableData[i].insurance_main_plans_payout}</td>
                       <td>${tableData[i].main_plan_id}</td>
                       <td>${tableData[i].startDate}</td>
                   </tr>
                `;

                $('#gfInsuranceMainPlansPayout-list-tbody').append(htmlString);
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// Get All Insurance Main Cash Plans function to display in table
function getAllGfMainCashPlans() {
    try {
        axios.get("http://127.0.0.1:6543/getAllGfMainCashPlans").then(query => {
            let tableData = query.data;
            console.log(tableData);

            for (var i = 0; i < tableData.length; i++) {
                var htmlString =
                    `
                   <tr data-active="N">
                       <td>${tableData[i].insurance_main_cash_plans_id}</td>
                       <td>${tableData[i].main_plan_id}</td>
                       <td>${tableData[i].dateCreated}</td>
                   </tr>
                `;

                $('#gfInsuranceMainCashPlans-list-tbody').append(htmlString);
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// Get All Insurance Main Plans Premium function to display in table
function getAllGfMainPlansPremium() {
    try {
        axios.get("http://127.0.0.1:6543/getAllGfMainPlansPremium").then(query => {
            let tableData = query.data;
            console.log(tableData);

            for (var i = 0; i < tableData.length; i++) {
                var htmlString =
                    `
                   <tr data-active="N">                      
                       <td>${tableData[i].insurance_main_plans_premium_schedule_id}</td>
                       <td>${tableData[i].main_plan_id}</td>
                       <td>${tableData[i].year}</td>
                   </tr>
                `;

                $('#gfInsuranceMainPlansPremiumSchedule-list-tbody').append(htmlString);
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// Get All Insurance Riders function to display in table
function getAllGfRiders() {
    try {
        axios.get("http://127.0.0.1:6543/getAllGfRiders").then(query => {
            let tableData = query.data;
            console.log(tableData);

            for (var i = 0; i < tableData.length; i++) {
                var htmlString =
                    `
                   <tr data-active="N">    
                       <td>${tableData[i].insurance_riders_id}</td>
                       <td>${tableData[i].mongodb_rider_id}</td>
                       <td>${tableData[i].main_plan_id}</td>
                       <td>${tableData[i].ageOfEntry}</td>
                       <td>${tableData[i].productName}</td>
                       <td>${tableData[i].insurer}</td>
                       <td>${tableData[i].policyNum}</td>
                   </tr>
                `;

                $('#gfInsuranceRiders-list-tbody').append(htmlString);
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// Get All Insurance Riders Premium function to display in table
function getAllGfRidersPremium() {
    try {
        axios.get("http://127.0.0.1:6543/getAllGfRidersPremium").then(query => {
            let tableData = query.data;
            console.log(tableData);

            for (var i = 0; i < tableData.length; i++) {
                var htmlString =
                    `
                   <tr data-active="N">
                       <td>${tableData[i].insurance_riders_premium_schedule_id}</td>
                       <td>${tableData[i].rider_id}</td>
                       <td>${tableData[i].main_plan_id}</td>
                       <td>${tableData[i].year}</td>
                   </tr>
                `;

                $('#gfInsuranceRidersPremiumSchedule-list-tbody').append(htmlString);
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// Call all the functions above
getAllGfUser();
getAllGfMainPlans();
getAllGfMainPlansPayout();
getAllGfMainCashPlans();
getAllGfMainPlansPremium();
getAllGfRiders();
getAllGfRidersPremium();