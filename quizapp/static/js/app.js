var app = angular.module('quizApp',['ui.bootstrap','checklist-model']);

//constant and global function.
var WRONG = "danger";
var RIGHT = "";
var normalizeText = function(text){
	while(text.search(' ')!=-1||text.search('&')!=-1){
		text = text.replace(" ",'').replace('&','');
	}
	return text.toLowerCase();
}
var maxQuestion = 9;
//config http provider to post easyly
app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
//init root variables
app.run(function($rootScope) {
	$rootScope.name = "hello";
	$rootScope.option = "menu";
	$rootScope.category = "''";
	$rootScope.changeTo = function(str){
    	$rootScope.option = str;
    };
    
});
//menu items in menu
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
//profile page
app.directive("profile",function(){
	return{
		restrict: "E",
		controller: ['$scope','$http','$rootScope',function($scope,$http,$rootScope){
			//get avatars list
			$http.get('static/json/avatars.json').success(function(data) {
			        $scope.avatars = data;
			    });
			$scope.backToMenu = function(){
				$rootScope.option = "menu";
			};
			//get data
			$http.get('getuserinfor').success(function(data) {
				$scope.user = data;
			});
			//confirm, send user information then back to menu
			$scope.confirm = function(){
				$http({
					method: 'POST',
					url: '/profile/',
					headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    				transformRequest: function(obj) {
	       				 var str = [];
	        			for(var p in obj)
	        			str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
	        			return str.join("&");
    				},
					data: $scope.user
				}).then(function(){
					$scope.backToMenu();
				});
			}
		}],
		scope: {},
		templateUrl: 'static/profile.html'
	}
});
//directive for startup screen
app.directive("startupScreen",function(){
	return{
		restrict: "E",
		controller: ['$scope','$rootScope','$http','$interval',function($scope,$rootScope,$http,$interval){
			$scope.inProcess = false;
			$scope.isAnswering = false;
			$scope.category = normalizeText($scope.title);
			$scope.likes = [];
			$scope.dislikes = [];
			$http.get('getuserinfor').success(function(data) {
				$scope.user = data;
			});
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
				$scope.userScore = 0;
				$scope.timer = null;
				$scope.userAnswers = [];
				$scope.userAnswers[0] = -1;
				$http.get('getquestionlist/' + $scope.category).success(function(data) {
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
				if($scope.currentQuestion>maxQuestion){
					$scope.numberOfRightAnswer = getNumberOfRightAnswer();
					$scope.currentQuestion--;
					$scope.isAnswering = false;
					$scope.end = true;
					postScore();
				}else{
    			    $scope.inProcess = true;
					$scope.isAnswering = true;
				}
				$interval.cancel($scope.showResult);
			};
			$scope.showDetailResult = function(){
				$scope.isAnswering = true;
				$scope.end = true;
			};
			var postScore = function(){
				var sScore = $scope.userScore.toString();
				$scope.data = {
					score: sScore
				};
				$http({
					method: 'POST',
					url: '/updatescore/',
					headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    				transformRequest: function(obj) {
	       				 var str = [];
	        			for(var p in obj)
	        			str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
	        			return str.join("&");
    				},
					data: $scope.data
				}).then();
			};
			$scope.resetProcess = function(){
				$scope.inProcess = false;
			};
			$scope.confirmAnswer = function(){	
				if($scope.userAnswers[$scope.currentQuestion]<0) return;
    			if(checkAnswer()){
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
			var checkAnswer = function(){
				if($scope.questions[$scope.currentQuestion].type=='multi-select'){
					if ($scope.userAnswers[$scope.currentQuestion].length!=$scope.questions[$scope.currentQuestion].answer.length) return false;
					$scope.userAnswers[$scope.currentQuestion].sort(function(a, b){return a-b});
					for(i = 0;i<$scope.questions[$scope.currentQuestion].answer.length;i++)
						if($scope.questions[$scope.currentQuestion].answer[i]!=$scope.userAnswers[$scope.currentQuestion][i]) return false;
					return true;
				}
				else if($scope.questions[$scope.currentQuestion].type=='fill-two-blanks'){
					for(i = 0;i<$scope.questions[$scope.currentQuestion].answer.length;i++)
						if($scope.questions[$scope.currentQuestion].answer[i]!=$scope.userAnswers[$scope.currentQuestion][i]) return false;
					return true;
				}
				else{
					if($scope.userAnswers[$scope.currentQuestion]==$scope.questions[$scope.currentQuestion].answer) return true;
					else return false;
				}
			}
			$scope.vote = function(votedArray,reverseArray,id){
				var i = votedArray.indexOf(id);
				var j = reverseArray.indexOf(id);
				if(i==-1&&j==-1) votedArray.push(id);
				else if (i!=-1) votedArray.splice(i, 1);
				else if (j!=-1){
					reverseArray.splice(j, 1);
					votedArray.push(id);
				}
			}
			$scope.postVote = function(){
				$scope.voteData = {
					votelist: '',
					dislike:''
				};
				$scope.voteData.votelist = $scope.likes.join();
				$scope.voteData.dislike = $scope.dislikes.join();
				$http({
					method: 'POST',
					url: '/questionrate/',
					headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    				transformRequest: function(obj) {
	       				 var str = [];
	        			for(var p in obj)
	        			str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
	        			return str.join("&");
    				},
					data: $scope.voteData
				}).then();
				$scope.resetProcess();
			}
			$scope.getColorClass = function(array,id){
				if(array.indexOf(id)==-1) return 'unactive';
				else return 'active';
			}
		}],
		scope: {
			title: "="
		},
		templateUrl: 'static/startup-screen.html'
	}
});

app.directive('leaderboard',function(){
	return{
		restrict: "E",
		controller: ['$scope','$rootScope','$http',function($scope,$rootScope,$http){
			$http.get('getleaderboard').success(function(data) {
				$scope.players = data;
			});
			$scope.backToMenu = function(){
				$rootScope.option = "menu";
			};
		}],
		templateUrl: 'static/leaderboard.html'
	};
});

app.directive('profileBar',function(){
	return{
		restrict: "E",
		controller: ['$scope','$rootScope','$http',function($scope,$rootScope,$http){
			$http.get('getuserinfor').success(function(data) {
				$scope.user = data;
			});
		}],
		templateUrl: 'static/profile-bar.html'
	}
});