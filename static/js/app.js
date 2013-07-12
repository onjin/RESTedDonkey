'use strict';

/* App Module */

angular.module('donkey', ['resourceFilters', 'resourceServices']).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/resources', {
          templateUrl: '/_static/partials/resource-list.html',
          controller: ResourceListCtrl
      }).
      when('/resources/:resourceId', {
          templateUrl: '/_static/partials/resource-detail.html',
          controller: ResourceDetailCtrl
      }).
      otherwise({redirectTo: '/resources'});
}]);
