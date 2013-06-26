'use strict';

/* Services */

angular.module('resourceServices', ['ngResource']).
    factory('Resource', function($resource){
  return $resource('resources/:resourceId.json', {}, {
    query: {method:'GET', params:{resourceId:'_list'}, isArray:true}
  });
});
