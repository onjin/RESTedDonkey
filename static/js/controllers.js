'use strict';

/* Controllers */

function ResourceListCtrl($scope, Resource) {
  $scope.resources = Resource.query();
  $scope.orderProp = 'name';
}

//ResourceListCtrl.$inject = ['$scope', 'Resource'];



function ResourceDetailCtrl($scope, $routeParams, Resource) {
  $scope.resource = Resource.get({resourceId: $routeParams.resourceId}, function(resource) {
    //$scope.mainImageUrl = phone.images[0];
  });

  $scope.setImage = function(imageUrl) {
    $scope.mainImageUrl = imageUrl;
  }
}

//ResourceDetailCtrl.$inject = ['$scope', '$routeParams', 'Resource'];
