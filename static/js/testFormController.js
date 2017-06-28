//Definindo a Controller
angular.module("pythonCrawler").controller("testFormController", function ($scope, $http) {
	
	//Função para contar o número de ocorrências
	$scope.contarOcorrencias = function(){
		//Fazer o GET na API
		$http.get(urlBase + "/api/ocorrencias/" + $scope.criterio + "/" + $scope.url).then(function(response){
			//Se a a requisição der certo

			//Passar a resposta para o $scope
			$scope.ocorrencias = response.data.ocorrencias;

		},function(response){
			//Se a requisição falhar
			$scope.ocorrencias = response.data.ocorrencias;
		})
	}

});
