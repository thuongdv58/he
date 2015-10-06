var app = angular.module('quizApp',['ui.bootstrap']);
app.run(function($rootScope) {
	$rootScope.option = "menu";
	$rootScope.category = "'Sports'";
	$rootScope.changeTo = function(str){
    	$rootScope.option = str;
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
app.directive('leaderboard',function(){
	return{
		restrict: "E",
		controller: ['$scope','$rootScope','$http',function($scope,$rootScope,$http){
			$http.get('json/leaderboard.json').success(function(data) {
				$scope.players = data;
				$scope.xsize = 2;
			});
			$scope.backToMenu = function(){
				$rootScope.option = "menu";
			}
			
		}],
		templateUrl: 'leaderboard.html'
	};
})