function calculateCTc() {
    var ctc;
    var sex = document.getElementsByName("sex");
    var patients_age = document.getElementById("patients-age").value;
    var patients_weight = document.getElementById("patients-weight").value;
    var patients_height = document.getElementById("patients-height").value;
    var patients_serum = document.getElementById("patients-serum").value;
    var ctcResult = document.getElementById("ctc");
    var warning = document.getElementById("warning");
    var resultsContainer = document.getElementById("ctc-results");
    var selectedSex;
    var formatctc;
    var errorstr;
    var warningstr;

    resultsContainer.style.display = "block";
    
    //refresh the values
    selectedSex = "";
    errorstr = "";
    ctcResult.innerHTML = "";
    warning.innerHTML = "";
    warningstr = "";
    //alert(patients_age.length==0);
    
    //check validity of each variable (sex is combined with weight adjustment)
    if(!sex[0].checked && !sex[1].checked){
        errorstr = errorstr.concat("Sex is not selected. <br/>");
    }
    else{
        for(var i=0; i<sex.length; i++) {
            if(sex[i].checked) selectedSex = sex[i].value;
        }
    }


    if(patients_age.length == 0 || patients_age.charAt(0) == "-"){
        errorstr = errorstr.concat("Age input is not a valid number. <br/>");
    }
    else if(patients_age.length > 0 || patients_age.charAt(0)!= "-"){
        patients_age = parseFloat(patients_age);
        if(patients_age<=12){
            errorstr = errorstr.concat("This equation should not be used to calculate renal function of children under 12. <br/>");
        }
        if(patients_age>70){
            errorstr = errorstr.concat("This equation should not be used to calculate renal function of people over 70. <br/>");
        }
    }


    if(selectedSex == ""){
        if(patients_weight.length == 0 || patients_weight.charAt(0)=="-"){
            errorstr = errorstr.concat("Weight input is not a valid number. <br/>");
        }
        if(patients_height.length == 0 || patients_height.charAt(0)=="-"){
            warningstr = warningstr.concat("Height input is not a valid number. <br/>");
        }
    }
    else{
        if((patients_weight.length > 0 && patients_weight.charAt(0)!= "-") && (patients_height.length > 0 && patients_height.charAt(0)!="-")){
            patients_weight = parseFloat(patients_weight);
            patients_height = parseFloat(patients_height);
            BMI = patients_weight/(patients_height)/(patients_height)*10000;
            
            if(patients_height<50){
                errorstr = errorstr.concat("Height is too low. Please double check. <br/>");
            }

            if(patients_height>=200){
                errorstr = errorstr.concat("Height is too high. Please double check. <br/>");
            }

            if(patients_weight<20){
                errorstr = errorstr.concat("Weight is too low. Please double check. <br/>");
            }

            if(patients_weight>=200){
                errorstr = errorstr.concat("Weight is too high. Please double check. <br/>");
            }
            
            // calculate ideal body weight
            IBW = 2.3*((patients_height/2.54)-60);
            if(selectedSex=='m'){
                IBW = IBW + 50;
            }
            else if(selectedSex=='f'){
                IBW = IBW + 45.5;
            }

            // assign modified BW accordingly
            if(BMI>=25){
                //assign weight as adjusted BW
                patients_weight = IBW + 0.4*(patients_weight-IBW);
                warningstr = warningstr.concat("BMI is high. Adjusted BW is implemented. <br/>");
            }
            else if(BMI<18.5){
                patients_weight = patients_weight;
            }
            else{
                patients_weight = IBW;
            }
        }
        else{
            if(patients_weight.length == 0 || patients_weight.charAt(0)=="-"){
                errorstr = errorstr.concat("Weight input is not a valid number. <br/>");
                if(patients_height.length == 0 || patients_height.charAt(0)=="-"){
                    errorstr = errorstr.concat("Height input is not a valid number. <br/>");
                }
            }
            else{
                patients_weight = parseFloat(patients_weight);
                if(patients_height.length == 0){
                    warningstr = warningstr.concat("Height input is none.");
                    if(((patients_age.length > 0 && patients_age.charAt(0)!="-")&&(patients_weight.length > 0 && patients_weight.charAt(0)!="-"))&&(patients_serum.length > 0 && patients_serum.charAt(0)!="-")){
                        warningstr = warningstr.concat("The calculation shall proceed without adjusting body weight.");
                    }
                    warningstr = warningstr.concat("<br/>");
                }
                else if(patients_height.charAt(0)=="-"){
                        errorstr = errorstr.concat("Height input is not a valid number. <br/>");
                    }
            }
        }
    }


    if(patients_serum.length==0 || patients_serum.charAt(0)=="-"){
        errorstr = errorstr.concat("Serum creatinine input is not a valid number. <br/>");
    }
    else if(patients_serum.length>0 || patients_serum.charAt(0)!="-"){
        patients_serum = parseFloat(patients_serum);
        if(patients_serum<=30){
            errorstr = errorstr.concat("Serum creatinine is too low. Please double check the unit. <br/>");
        }
        if(patients_serum>500){
            errorstr = errorstr.concat("Serum creatinine is too high. Please double check. <br/>");
        }
    } 
    
    if(errorstr==""){
        
        ctc = ((parseFloat(140)-patients_age) * patients_weight) /(patients_serum *0.8);

        if (selectedSex == 'f') {
            ctc = parseFloat(ctc) * parseFloat(0.85);
        }

        formatctc = parseFloat(ctc).toFixed(2);
        warning.style.color = "red";
        warning.innerHTML = warningstr;
        ctcResult.innerHTML = "Creatinine Clearance (Cockcroft-Gault Equation): ".concat(String(formatctc)," mL/min.");
    }
    else{
        warning.style.color = "red";
        warning.innerHTML = errorstr.concat(warningstr);
    }
}

function clrcal(){
    var sex = document.getElementsByName("sex");
    var patients_age = document.getElementById("patients-age");
    var patients_weight = document.getElementById("patients-weight");
    var patients_height = document.getElementById("patients-height");
    var patients_serum = document.getElementById("patients-serum");
    var ctcResult = document.getElementById("ctc");
    var warning = document.getElementById("warning");
    var resultsContainer = document.getElementById("ctc-results");

    for(var i=0;i<sex.length;i++)
        sex[i].checked = false;
    patients_age.value="";
    patients_weight.value="";
    patients_height.value="";
    patients_serum.value="";
    ctcResult.value="";
    warning.value="";
    resultsContainer.style.display = "none";
}

function modcal(){
    var ctcResult = document.getElementById("ctc");
    var warning = document.getElementById("warning");
    var resultsContainer = document.getElementById("ctc-results");

    ctcResult.value="";
    warning.value="";
    resultsContainer.style.display = "none";
}