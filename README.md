<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/imcarlosguerrero/mongodb-atlas-data-api">
    <img src="https://i.imgur.com/8P9wZJT.png" alt="Logo" width="250">
  </a>

  <h3 align="center">MongoDB Atlas Data API - Python Integration</h3>

  <p align="center">
    A simple <strong>Python</strong> Integration with the <strong>MongoDB Atlas Data API.</strong> It's useful in <a href="https://www.mongodb.com/docs/atlas/api/data-api/#when-to-use-the-data-api"><strong>certain scenarios.</strong></a>
    <br />
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Sometimes using official drivers such as <a href="https://www.mongodb.com/docs/drivers/pymongo/"><strong>PyMongo</strong></a> can lead to limiting cases such as:

* You want to run MongoDB operations from a web application or other client that you can't trust, this by limiting the scope of your <a href="https://www.mongodb.com/docs/atlas/api/data-api/#data-access-permissions"><strong>Data API Access Key</strong></a>.
* You can't or don't want to manage a MongoDB driver in your server-side environment. For example, the hosting you are using is blocking <a href="https://www.mongodb.com/docs/manual/reference/connection-string/#dns-seed-list-connection-format"><strong>mongodb + srv</strong></a> connections, therefore, your unique alternative is using an <a href="https://www.mongodb.com/docs/atlas/api/data-api/#read-and-write-with-the-data-api"><stro-ng>http endpoint</strong></a>.
* You want to develop a new feature and prefer a flexible solution for working on the client side first before later creating and refining the API layer.
* Your hosting doesn't provide a supported <a href="https://www.cloudflare.com/learning/ssl/how-does-ssl-work/"><strong>TLS/SSL</strong></a> version to entrust a connection with <a href="https://www.mongodb.com/atlas/database"><strong>Atlas</strong></a> as documented <a href="https://pymongo.readthedocs.io/en/stable/atlas.html"><strong>here<strong></a>. 

Of course, there are more scenarios where this implementation is useful, such as the described in the <a href="https://www.mongodb.com/docs/atlas/api/data-api/#when-to-use-the-data-api"><strong>official data api documentation.</strong></a> Using some of the endpoints listed there can be enough for most people, but when you have to use many of them, many times you can begin to think that having a wrapper class around the <a href="https://www.mongodb.com/docs/atlas/api/data-api-resources/"><strong>api resources</strong></a> and that's what this library is, an easy to use collection of utilities with the <a href="https://www.mongodb.com/docs/manual/crud/"><strong>basic operations</strong></a> of MongoDB.

<!-- GETTING STARTED -->
## Getting Started

### Installation

Install and update using <a href="https://pip.pypa.io/en/stable/getting-started/"><strong>pip</strong></a>:
   ```sh
   pip install -U mongodb_atlas_data_api
   ```

<!-- USAGE EXAMPLES -->
### Usage

First, you have to enable the Data API on your MongoDB Atlas Cluster, you can do this by clicking the Data API option in Services section at the left panel in your Cluster Options.
<br>
</br>
<a href="https://github.com/imcarlosguerrero/mongodb-atlas-data-api">
    <img src="https://i.imgur.com/xidYOOS.jpg" alt="Enable Data API">
  </a>
<br>
</br>
After, create a key and copy it into a safe place, note that you can also limit the <a href="https://www.mongodb.com/docs/atlas/api/data-api/#data-access-permissions"><strong>Data API Access</strong></a>, this is useful specially if you don't trust the hosting you're using and would like to limit the problem that a leak of this key could mean.
<br>
</br>
  <div align="center">
<img src="https://i.imgur.com/9mTEYKO.gif">
</div>
<br>
</br>
Once you have a key you can create a <strong>MongoOperator</strong> object by calling it from the <strong>mongodb_atlas_data_api</strong> library, this object receives five parameters, which are listed below:
<br>
</br>

| Type        | Necessity | Description                                           |
|-------------|-----------|-------------------------------------------------------|
| data_api    | Required | The main endpoint for accessing the API               |
| access_key  | Required | A unique key that is used to authenticate requests    |
| data_source | Required | The name of the cluster                                |
| database    | Required | The name of the database within the cluster            |
| collection  | Required | The name of the collection within the database        |
</br>

Once you have created a <strong>MongoOperator</strong> object you can use all the <a href="https://www.mongodb.com/docs/atlas/api/data-api-resources/"><strong>available operations</strong></a>, all of these operations are well described in the <a href="https://www.mongodb.com/docs/atlas/api/data-api-resources/"><strong>official documentation</strong></a>, you can lean on here if you  got questions that are not answered here.

<!-- CODE EXAMPLE -->
### Code Example

   ```python
   # test.py
   
from mongodb_atlas_data_api import MongoOperator
   
mongoOperator = MongoOperator(
	data_api="<your-data-api>", 
	access_key="<your-access-key>", 
	data_source="<your-cluster-name/data-source-name>", 
	database="<your-database>", 
	collection="<your-collection>"
)

find = mongoOperator.find_one(filter={"id": 1}, projection={"_id": 0})
print(find)
   ```
### Run Code	
 ```sh
 $ python test.py
   ```
### Result
 ```sh
{'document': {'id': 1, 'text': "Everything's Working :)"}}
   ```

<!-- GETTING STARTED -->
## Note

Expressions such as <a href="https://www.mongodb.com/docs/manual/tutorial/query-documents/"><strong>Query Filter</strong></a>, <a href="https://www.mongodb.com/docs/manual/tutorial/update-documents"><strong>Update Expression</strong></a>, <a href="https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/"><strong>Query Projection</strong></a>, <a href="https://www.mongodb.com/docs/manual/core/aggregation-pipeline/"><strong>Aggregation Pipeline</strong></a>, and more, are fully supported, so don't worry 	 using those expression with this library.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [MongoDB Atlas Data API Documentation](https://www.mongodb.com/docs/atlas/api/data-api)
