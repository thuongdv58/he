var app = angular.module('quizApp',['ui.bootstrap']);
app.run(function($rootScope) {
	$rootScope.option = "menu";
	$rootScope.category = "'Sports'";
	$rootScope.changeTo = function(str){
    	alert("change to "+ str);
    	$rootScope.option = "profile";
    };
   
    
	
})
app.controller('menuController', ['$scope', '$http','$attrs',
  function ($scope, $http, $attrs) {
    $http.get('json/userinfo.json').success(function(xdata) {
        $scope.user = xdata;
    });
}])

app.directive('menuItem',function(){
	return{
		restrict: "EA",
		controller: ['$scope','$rootScope',function($scope,$rootScope){
			 $scope.enterStartupScreen = function(str){
			    	$rootScope.category = str;
			    	$rootScope.option = "answer";
			 };
		}],
		scope: {
			item: "="
		},
		templateUrl: 'menu-item.html'
	};
})
app.directive("startupScreen",function(){
	return{
		restrict: "E",
		controller: ['$scope','$rootScope','$http',function($scope,$rootScope,$http){
			$scope.inProcess = false;
			$scope.backToMenu = function(){
				$rootScope.option = "menu";
			}
			$scope.beginAnswer = function(){
				$http.get('json/'+category+'question.json').success(function(data) {
			        $scope.questions = data;
			    });
			}
			
		}],
		scope: {
			category: "="
		},
		templateUrl: 'startup-screen.html'
	}
})