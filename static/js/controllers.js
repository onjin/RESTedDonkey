'use strict';

/* Controllers */

function ResourceListCtrl($scope, Resource) {
    $scope.resources = Resource.query();
    $scope.orderProp = 'name';
}

//ResourceListCtrl.$inject = ['$scope', 'Resource'];



function ResourceDetailCtrl($scope, $routeParams, Resource) {
    $scope.resource = Resource.get({resourceId: $routeParams.resourceId}, function(resource) {
        // pass
    });
    $scope.addResource = function() {
        todoFactory.save($scope.newTodoModel, backToList);
    }

}

//ResourceDetailCtrl.$inject = ['$scope', '$routeParams', 'Resource'];
