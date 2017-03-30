// AngularJS app File

// Create new module containing the differnt components of the AngularJS app
var app = angular.module("ThumbnailApp", []);

// Manage app data
app.controller('ThumbnailCtrl', ['$scope','thumbnails', function($scope, thumbnails) {
    // Use thumbnails service to fetch data asynchronously from API
    thumbnails.then(function(data) {
        
        // Store thumbnail data for use in view
        $scope.thumbnailsObj = data;
    });
 
}]);