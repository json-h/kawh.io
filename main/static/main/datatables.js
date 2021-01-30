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

    $('#all-players-avg').DataTable( {
      "autowidth": true,
      "bFilter": false,
      "bPaginate": false,
      "bInfo": false,
      "aoColumns": [
        null,
        null,
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
        { "orderSequence": [ "desc" ] },
      ]
    } );

    $('#all-players-std').DataTable( {
      "autowidth": true,
      "bFilter": false,
      "bPaginate": false,
      "bInfo": false,
      "aoColumns": [
        null,
        null,
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
        { "orderSequence": [ "asc" ] },
      ]
    } );
    
  } );