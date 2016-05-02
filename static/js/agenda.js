//  OUR ANG APP
var agenda = angular.module('agendaMaker',[]);

//  CONTROLLERS
agenda.controller('agenda_input',['$scope','$http','ajaxService',function($scope, $http, ajax){
   var agenda = this;


}]);


//  SERVICES
agenda.service('ajaxService',
function($http, $q){
  // public API
  return({
    getAgenda: getAgenda,
    saveAgendaItem: saveAgendaItem
  });

  function getAgenda (){
    var req = $http({
      method: "post",
      url: "/get_agenda_items/"
    });

    return( req.then(handleSuccess, handleError) );

  };

  function saveAgendaItem(){
    console.log( $scope.agendaMaker.agenda_item );
  };

  //  PRIVATE METHODS

  function handleError( response ) {
      if (
          ! angular.isObject( response.data ) ||
          ! response.data.message
          ) {
          return( $q.reject( "An unknown error occurred." ) );
      }
      return( $q.reject( response.data.message ) );
  };

  function handleSuccess( response ) {
    return( response.data );
  };

});

// FILTERS

agenda.filter('meetingOrder',function(){
    return function(items){
        var out = [];
        // TODO: sort by meeting name
        for (i in items){
            out.push(i);
        }
    }
});


