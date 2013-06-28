'use strict';

/* Services */

angular.module('resourceServices', ['ngResource']).

factory('Resource', function($resource){
    return $resource('/_manager/resources/:resourceId');
});
