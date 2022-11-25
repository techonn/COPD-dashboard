function print_summary_as_pdf() {
    //declare element to print
    //var content_page = document.getElementById("printable_content").cloneNode(true);
    var container= document.createElement('div');
    var pageheader= document.getElementById("page-header").cloneNode(true);
    var flashcards= document.getElementById("flashcards").cloneNode(true);
    flashcards.style.margin = "auto";

    var chartCanvas = document.getElementById("bar-chart");
    while (chartCanvas == null || chartCanvas.style.length < 1) {
        true==true;
      }
    var imageElement = document.createElement("img");
    imageElement.style = "width: 100%;";
    imageElement.src = chartCanvas.toDataURL("image/png", 0);

    var barheader= document.getElementById("barheader").cloneNode(true);

    var barchart= document.createElement('div');
    barchart.innerHTML = "<div class='col-xl-12 col-lg-7'><div class='card shadow mb-4'>" + barheader.outerHTML + imageElement.outerHTML + "</div></div></div>";
    barchart.classList.add('row');
    barchart.style.margin = "auto";

    var chartCanvasGP = document.getElementById("gp-bar-chart");
    while (chartCanvasGP == null || chartCanvasGP.style.length < 1) {
        true==true;
      }
    var GPimageElement = document.createElement("img");
    GPimageElement.style = "width: 100%;";
    GPimageElement.src = chartCanvasGP.toDataURL("image/png", 0);

    var GPbarheader= document.getElementById("GPbarheader").cloneNode(true);

    var GPbarchart= document.createElement('div');
    GPbarchart.innerHTML = "<div class='col-xl-12 col-lg-7'><div class='card shadow mb-4'>" + GPbarheader.outerHTML + GPimageElement.outerHTML + "</div></div></div>";
    GPbarchart.classList.add('row');
    GPbarchart.style.margin = "auto";
    GPbarchart.classList.add('pagebreak');

    var infectiondrug= document.getElementById("infectiondrug").cloneNode(true);
    infectiondrug.style.margin = "auto";

    var BNForitable= document.getElementById("BNForitable").cloneNode(true);
    BNForitable.style.margin = "auto";
    BNForitable.classList.add('pagebreak');

    var BNFaddtable= document.getElementById("BNFaddtable").cloneNode(true);
    BNFaddtable.style.margin = "auto";

    //add element to print

    container.style.margin = '10px';
    container.style.padding = '0px';
    container.style.display = "inline";
    container.style.fontSize = "12px";
    container.style.lineHeight = "1.2";

    //container.appendChild(content_page);
    container.appendChild(pageheader);
    container.appendChild(flashcards);
    container.appendChild(barchart);
    container.appendChild(GPbarchart);
    //container.appendChild(barcanvas);
    container.appendChild(infectiondrug);
    container.appendChild(BNForitable);
    container.appendChild(BNFaddtable);

    html2pdf(container,{
        margin: [15,10,15,10],
        filename: 'Summary.pdf',
        image: {type: 'jpeg', quality: 0.98},
        html2canvas: {scale: 2, logging: true, dpi: 192, letterRendering: true},
        pagebreak: {
            mode: ['css', 'whiteline'],
            avoid: ['img', '.row']
        },
        jsPDF: {unit: 'mm', format: 'a4', orientation: 'portrait'}
    });
}