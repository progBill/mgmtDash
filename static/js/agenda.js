//  OUR ANG APP
var agenda = angular.module('agendaMaker',[]);

//////////////////
//  CONTROLLERS //
//////////////////

agenda.controller('agenda_input',['$scope', 'ajaxService',function($scope, ajax){
    var agenda = this;

    ajax.getAgenda().then(
        function(d){
            $scope.agenda = d.data;
        });

    $scope.saveAgendaItem = function(){
        ajax.saveAgendaItem({topic: $scope.item.topic, meeting: $scope.item.meeting});
        $scope.agenda.push({'topic': $scope.item.topic, 'meeting': $scope.item.meeting, 'item_id':-1});
        $scope.item.topic= null;
        $scope.item.meeting = null;
    };

    $scope.removeItem = function( item ){
        var i = $scope.agenda.indexOf(item);
        if (i != -1){
            $scope.agenda.splice(i,1);
        }
        ajax.removeItem( item.item_id );
    };

}]);

///////////////
//  SERVICES //
///////////////

agenda.service('ajaxService',
function($http, $q){
  // public API
  return({
    getAgenda: getAgenda,
    saveAgendaItem: saveAgendaItem,
    removeItem: removeItem
  });

  function getAgenda (){
    var req = $http({
      method: "POST",
      url: "/mgmtDash/get_agenda_items"
    });

    return( req.then(handleSuccess, handleError) );
  };

  function saveAgendaItem(d){
    var req = $http({
      method: "POST",
      url: "/mgmtDash/create_agenda_item",
      data: d
    });

    return( req.then(handleSuccess, handleError));
  };

  function removeItem(id){
    var req = $http({
      method: "POST",
      url: "/mgmtDash/delete_agenda_item/" + id
    });
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
    return( response );
  };

});


