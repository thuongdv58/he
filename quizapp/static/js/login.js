/**
 * Created by trung on 10/12/2015.
 */
var app = angular.module('quizApp',['ui.bootstrap']);
app.controller('LogiController', function($scope){
    $scope.chekLogin = function(){
        var username = $scope.username;
        var password = $scope.password;
        alert("Username: "+username+'- Password: '+password);
    };
});