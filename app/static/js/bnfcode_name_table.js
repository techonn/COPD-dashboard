function BNFSearch() {
    var input = document.getElementById("myInput");
    var filter = input.value.toUpperCase();
    var Table = document.getElementById("table");
    var tr = Table.getElementsByTagName("tr")

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td_code = tr[i].getElementsByTagName("td")[0];
    td_name = tr[i].getElementsByTagName("td")[1];
    if (td_code||td_name) {
      txtValue = (td_code.textContent || td_code.innerText).concat(td_name.textContext||td_name.innerText);
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
</script>