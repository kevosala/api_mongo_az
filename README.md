# API Rest Flask CosmosDB Azure API MongoDB
API Rest desarrollada con el framework de Python Flask que se conecta a CosmosDB Azure API MongoDB

# Pasos para crear la BD en Azure:

## Creación de cuenta en Azure:
* Entrar al siguiente link: https://azure.microsoft.com/en-us/
* Clic en Sig In

![SigIn](https://user-images.githubusercontent.com/12562833/120581337-e3b3b880-c3e7-11eb-86cd-4b2dc03d14f0.png)

* Dar de alta una cuenta, o usar una cuenta existente
![Screenshot from 2021-06-02 21-17-49](https://user-images.githubusercontent.com/12562833/120581410-034ae100-c3e8-11eb-97bd-e5df531ab6c3.png)


## Entrar al portal de Azure
![Portal](https://user-images.githubusercontent.com/12562833/120581716-853b0a00-c3e8-11eb-8150-32a754e16153.png)

Esta es la página principal de Azure
![Screenshot from 2021-06-02 21-22-43](https://user-images.githubusercontent.com/12562833/120581835-ba475c80-c3e8-11eb-843a-61c2a401943b.png)


## Creación de recursos en Azure
* En la página principal de azure dar clic en Create a resource
![CreateResource](https://user-images.githubusercontent.com/12562833/120582109-2c1fa600-c3e9-11eb-9f4c-3f360146be42.png)

* Aparecerá la siguiente pantalla, en la barra de búsqueda enmarcada buscar * Resource group * y seleccionarlo:
![Search](https://user-images.githubusercontent.com/12562833/120582584-ec0cf300-c3e9-11eb-9cb5-78f6f015eab6.png)

Un grupo de recursos es un lugar donde se pueden administrar los recursos que se utilizarán en una aplicación.

* Clic en create
![Screenshot from 2021-06-02 21-32-21](https://user-images.githubusercontent.com/12562833/120582715-2f676180-c3ea-11eb-8799-6e4a82d3a715.png)

* Deberás asignar un nombre al grupo de recursos para poder identificarlo.
![Screenshot from 2021-06-02 21-40-44](https://user-images.githubusercontent.com/12562833/120583394-5f633480-c3eb-11eb-8af3-359bd1367dab.png)

* Seleccionar la región donde estará este recurso, lo recomendado es que se seleccione el más cercano a nuestra locación, por tema de redundancia.

* Clic en Review + Create 
![Screenshot from 2021-06-02 21-44-30](https://user-images.githubusercontent.com/12562833/120583640-e0223080-c3eb-11eb-81f5-a852589c31b0.png)

* Clic en Create

* Cuando el grupo de recursos se haya creado aparecerá lo siguiente:
![Screenshot from 2021-06-02 21-46-44](https://user-images.githubusercontent.com/12562833/120583914-4b6c0280-c3ec-11eb-8fc3-dec8096ac8a1.png)

*  Clic en Go to resource group

## Agregando el servicio de Azure CosmosDB al grupo de recursos creado.

*  Clic en Add
![Screenshot from 2021-06-02 21-50-32](https://user-images.githubusercontent.com/12562833/120584153-a7cf2200-c3ec-11eb-994b-d182976c908e.png)

* Aparecerá la siguiente pantalla, en la barra de búsqueda enmarcada buscar * Azure Cosmos DB * y seleccionarlo:
![Screenshot from 2021-06-02 21-52-01](https://user-images.githubusercontent.com/12562833/120584335-0a282280-c3ed-11eb-946d-1c192cfa64b9.png)

* Debemos seleccionar la API a trabajar, en este caso seleccionaremos Azure Cosmos DB API for MongoDB
![Screenshot from 2021-06-02 21-54-56](https://user-images.githubusercontent.com/12562833/120584504-570bf900-c3ed-11eb-83a1-c31049545bf4.png)

* Clic en Create

* Seleccionar el Resource Group creado
![RCdb](https://user-images.githubusercontent.com/12562833/120584948-1b256380-c3ee-11eb-919d-4a5bb3276426.png)

* Ingresar el nombre de la cuente de tu preferencia, seleccionar el capacity mode: Provisioned throughput y seleccionamos la última versión.
![Screenshot from 2021-06-02 21-59-33](https://user-images.githubusercontent.com/12562833/120585567-304ec200-c3ef-11eb-998f-ceb9da56ffda.png)

* Clic en Review + Create.

## Creación de BD y Colección
* Cuando termine el deployment dar clic en Go to resource
![Screenshot from 2021-06-02 22-10-05](https://user-images.githubusercontent.com/12562833/120585868-c256ca80-c3ef-11eb-9a9e-cc8b39e94d4e.png)

![Screenshot from 2021-06-02 22-13-47](https://user-images.githubusercontent.com/12562833/120586065-15308200-c3f0-11eb-8c3c-585ecb1398e6.png)

En la paǵina principal nos aparecerán las distintas formas de conectarnos a nuestra BD con diferentes lenguajes de programación

* Clic en Data Explorer
![Screenshot from 2021-06-02 22-17-18](https://user-images.githubusercontent.com/12562833/120586352-9d168c00-c3f0-11eb-9fd7-72e9dcbfdfac.png)

* Clic en New Database
![Screenshot from 2021-06-02 22-20-47](https://user-images.githubusercontent.com/12562833/120586549-f383ca80-c3f0-11eb-900b-6651a510ada1.png)

* Debes ingresar el nombre de tu base de datos y sleccionar la opción de Manual
* Clic en Ok

* La base de datos creada ahora aparecerá
![Screenshot from 2021-06-02 22-23-08](https://user-images.githubusercontent.com/12562833/120586753-4fe6ea00-c3f1-11eb-8593-612effdbc231.png)

* Dar clic en New Collection, para agregar nuestra colección a la BD
* Para obtener el PRIMARY CONNECTION debes dirigirte al panel izquierdo y seleccionar * Connection String * lo copias y lo pegas en la parte del código de Python donde se dejó comentado.

# Listo hemos creado la BD y colección en Azure Cosmos DB

### Si queres probar el código te recomiendo usar Postman te dejo el link para que lo veas https://www.postman.com/

# Si ya probaste que te funciona lo que te recomiendo es eliminar el grupo de recursos creado para no incurrir en gastos
* Debemos dar clic en el Home
* Seleccionar el grupo de recursos creado
![Screenshot from 2021-06-02 22-30-17](https://user-images.githubusercontent.com/12562833/120587225-35614080-c3f2-11eb-9794-c72d76fea20b.png)

Clic en * Delete resource group *

Debes ingresar el nombre del resource group 
![Screenshot from 2021-06-02 22-31-48](https://user-images.githubusercontent.com/12562833/120587353-6b062980-c3f2-11eb-9281-6cdab35c5dad.png)

Y por último clic en Delete

Si tienes alguna duda escribeme en Twitter @KevOoSalaz




