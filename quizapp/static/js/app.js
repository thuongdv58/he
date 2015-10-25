var app = angular.module('quizApp',['ui.bootstrap']);
var WRONG = "danger";
var RIGHT = "";
app.run(function($rootScope) {
	$rootScope.name = "hello";
	$rootScope.option = "menu";
	$rootScope.category = "'Sports'";
	$rootScope.changeTo = function(str){
    	$rootScope.option = str;
    };
    
	
});
app.controller('menuController',  ['$scope','$rootScope','$http',function($scope,$rootScope,$http){
	$scope.user = {
		name: "hello",
		kick: "hello",
		score: 10
	};
}]);

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
		templateUrl: 'static/menu-item.html'
	};
})
app.directive("startupScreen",function(){
	return{
		restrict: "E",
		controller: ['$scope','$rootScope','$http','$interval',function($scope,$rootScope,$http,$interval){
			$scope.userScore = 0;
			$scope.inProcess = false;
			$scope.isAnswering = false;
			$scope.userAnswer = "";
			$scope.addPoint = 0;
			$scope.backToMenu = function(){
				$rootScope.option = "menu";
			};
			$scope.beginAnswer = function(){
				$scope.end = false;
				$scope.currentQuestion = 0;
				$scope.inProcess = true;
				$scope.isAnswering = true;
				$scope.addPoint = 0;
				$scope.results = [];
				
				$scope.timer = null;
				$scope.userAnswers = [];
				$scope.userAnswers[0] = -1;
				$http.get('static/json/questionlist.json').success(function(data) {
			        $scope.questions = data;
			    });
			};
			var getNumberOfRightAnswer = function(){
				var count = 0;
				for (var i = 0; i < $scope.results.length; i++) {
					if($scope.results[i]!=WRONG) count++;
				};
				return count;
			};
			var addPointToScore = function(point){
				$scope.userScore += point;
			};
			var nextQuestion = function(){
				$scope.currentQuestion++;
				if($scope.currentQuestion>9){
					$scope.numberOfRightAnswer = getNumberOfRightAnswer();
					$scope.currentQuestion--;
					$scope.isAnswering = false;
					$scope.end = true;
				}else{
    			    $scope.inProcess = true;
					$scope.isAnswering = true;
					$scope.userAnswers[$scope.currentQuestion] = -1;
				}
				$interval.cancel($scope.showResult);
			};
			$scope.showDetailResult = function(){
				$scope.isAnswering = true;
				$scope.end = true;
			};
			$scope.resetProcess = function(){
				$scope.inProcess = false;
			};
			$scope.confirmAnswer = function(){	
				if($scope.userAnswers[$scope.currentQuestion]<0) return;
    			if($scope.userAnswers[$scope.currentQuestion]==$scope.questions[$scope.currentQuestion].answer){
    				$scope.addPoint = 10;
    				$scope.results[$scope.currentQuestion] = RIGHT;
    			}else{
    				$scope.addPoint = 0;
    				$scope.results[$scope.currentQuestion] = WRONG;
    			}		
    			addPointToScore($scope.addPoint);
    			$scope.isAnswering = false;
    			$scope.showResult = $interval(nextQuestion,1500);
			};
			
		}],
		scope: {
			category: "="
		},
		templateUrl: 'static/startup-screen.html'
	}
})
app.directive('leaderboard',function(){
	return{
		restrict: "E",
		controller: ['$scope','$rootScope','$http',function($scope,$rootScope,$http){
			$http.get('static/json/leaderboard.json').success(function(data) {
				$scope.players = data;
			});
			$scope.backToMenu = function(){
				$rootScope.option = "menu";
			}
			
		}],
		templateUrl: 'static/leaderboard.html'
	};
})
