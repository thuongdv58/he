var app = angular.module('quizApp',['ui.bootstrap']);
app.run(function($rootScope) {
	$rootScope.option = "menu";
	$rootScope.changeTo = function(str){
    	alert("change to "+ str);
    	$rootScope.option = "profile";
    }
});
app.controller('menuController', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('json/userinfo.json').success(function(xdata) {
        $scope.user = xdata;
    });
}])

app.directive('menuItem',function(){
	return{
		restrict: "E",
		scope: {
			item: "="
		},
		templateUrl: 'menu-item.html'
	};
})
