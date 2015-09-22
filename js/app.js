var app = angular.module('quizApp', []);
app.directive('quiz', function() {
    return {
	restrict: 'AE',
	scope: {},
	templateUrl: 'directive\questionpanels.html',
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
app.directive ('leaderboard',function(){
    return {
        restrict:'AEC',
        scope:{},
        templateUrl:'directive\leaderboard.html',
    }
});
app.directive ('profile',function(){
    return {
        restrict:'AEC',
        scope:{},
        templateUrl:'directive\profile.html',
    }
});
app.directive ('category',function(){
    return {
        restrict:'AEC',
        scope:{},
        templateUrl:'directive\category.html',
    }
});
app.controller("globalcontroller",function(){
    this.option=opt;
    this.startanswer=function(val)
    {
        this.option.quizanswer=true;
        this.option.quizanswer=val;
        this.option.menu=false;
    }
    this.backtomenu=function()
    {
        this.option.menu=true;
        this.option.leaderboard=false;
        this.option.profile=false;
        this.option.answer=false;
        this.option.login=false;
    }
    this.viewleaderboard=function()
    {
        this.option.leaderboard=true;
        this.option.menu=false;
    }
    this.editprofile=function()
    {
        this.option.profile=true;
        this.option.menu=false;
    }
});
var opt={
    login:false,
    menu:false,
    answer:false,
    leaderboard:false,
    profile:true,
    quizanswer:'none',
};
