var app = angular.module('quizApp', []);
app.directive('quiz', function() {
    return {
	restrict: 'AE',
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
app.directive ('leaderboard',function(){
    return {
        restrict:'AEC',
        scope:{},
        templateUrl:'leaderboard.html',
    }
});
app.directive ('profile',function(){
    return {
        restrict:'AEC',
        scope:{},
        templateUrl:'profile.html',
    }
});
app.controller("globalcontroler",function(){
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
var option={
    login:true;
    menu:false;
    answer:false;
    leaderboard:false;
    profile:false;
    quizanswer:'none';
}
});
