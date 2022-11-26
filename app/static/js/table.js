function createTable(tableData, elementid, filter) {
    var tableBody = document.getElementById(elementid);
    tableBody.innerHTML="";
    tableData.forEach(function(rowData) {
      //check if render of not
        var valid=false;
        var iter=0;
        var row = document.createElement('tr');
        rowData.forEach(function(cellData) {
            var cell = document.createElement('td');
            if(iter==4){
                cellData = parseFloat(cellData).toFixed(2);
                cell.appendChild(document.createTextNode(cellData));
            }
            else{
                cell.appendChild(document.createTextNode(cellData));
            }
            if(iter>0){
                if(iter!=1){
                    cell.classList.add('val');
                }
                row.appendChild(cell);
            }
            if(iter==1){
                if(String(cellData).toUpperCase().indexOf(filter)>-1){
                    valid=true;
                }
            }
            if(iter==0){
                if(String(cellData).toUpperCase().indexOf(filter)==0){
                    valid=true;
                }
            }
            iter = iter+1;
            });
        if(valid==true){
            tableBody.appendChild(row);
        }
    });
}