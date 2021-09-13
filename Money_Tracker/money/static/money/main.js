var elems = document.getElementsByClassName('confirmation');
var confirmIt = function (e) {
    if (!confirm('Are you sure?')) e.preventDefault();
};
for (var i = 0, l = elems.length; i < l; i++) {
    elems[i].addEventListener('click', confirmIt, false);
}







// Green/Red colors on budget summary based on value
var sumTable = document.getElementById('summaryTable');
for (var i = 1; i < sumTable.rows.length; i++){
    // console.log(sumTable.rows[i].cells.length)
    var leftOver = sumTable.rows[i].cells[3]; 
    if (parseInt(leftOver.innerHTML.slice(1)) > 0) {
        leftOver.style.backgroundColor = "#34ed43";   
    }
    else {
        leftOver.style.backgroundColor = "#f37d7d";  
    }
}