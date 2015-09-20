var app = angular.module('quizApp', []);
app.directive('quiz', function() {
    return {
	restrict: 'E',
	scope: {},
	templateUrl: 'questionpanels.html',
	link: function(scope, elem, attrs) {
            scope.start = function() {
                scope.Done=false;
                scope.inProgress=true;
			};
			scope.getQuestion = function() {
			};
            scope.finish =function()  {
            };
            scope.checkanswer =function()  {      
            };
	}
    }
});