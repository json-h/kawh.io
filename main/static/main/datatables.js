$(document).ready(function() {
    
    $('table.table.no-page').DataTable( {
      "autowidth": true,
      "bFilter": false,
      "bPaginate": false,
      "bInfo": false,
    } );  

    $('table.table.has-page').DataTable( {
      "autowidth": true,
      "bFilter": false,
    } );
    
  } );