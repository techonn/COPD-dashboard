function calculateCTc() {
    var ctc;
    var sex = document.getElementsByName("sex");
    var patients_age = parseFloat(document.getElementById("patients-age").value);
    var patients_weight = parseFloat(document.getElementById("patients-weight").value);
    var patients_serum = parseFloat(document.getElementById("patients-serum").value);
    var ctcResult = document.getElementById("ctc");
    var resultsContainer = document.getElementById("ctc-results");
    var formatctc;

    resultsContainer.style.display = "block";

    for(var i=0; i<sex.length; i++) {
        if(sex[i].checked) var selectedSex = sex[i].value;
    }

    ctc = ((parseFloat(140)-patients_age) * patients_weight) /(patients_serum *parseFloat(72));

    if (selectedSex == 'f') {
        ctc = parseFloat(ctc) * parseFloat(0.85);
    }

    formatctc = parseFloat(ctc).toFixed(2);
    ctcResult.innerHTML = formatctc;

}
