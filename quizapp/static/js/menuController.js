var app = angular.module('quizApp,[]);
app.directive('category', function(){
  return {
      restrict: 'E',
      scope: {
         name: '=type'
      },
      templateUrl: 'category.html'
  }
})