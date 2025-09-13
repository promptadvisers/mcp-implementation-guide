# Indexing overview

export const word_0 = "records"

This page describes key concepts related to indexing data in Pinecone.

## Indexes

In Pinecone, you store vector data in indexes. There are two types of indexes: dense and sparse.

### Dense indexes

Dense indexes store dense vectors, which are a series of numbers that represent the meaning and relationships of text, images, or other types of data. Each number in a dense vector corresponds to a point in a multidimensional space. Vectors that are closer together in that space are semantically similar.

When you query a dense index, Pinecone retrieves the dense vectors that are the most semantically similar to the query. This is often called **semantic search**, nearest neighbor search, similarity search, or just vector search.

Learn more:

* [Create a dense index](/guides/index-data/create-an-index#create-a-dense-index)
* [Upsert dense vectors](/guides/index-data/upsert-data#upsert-dense-vectors)
* [Semantic search](/guides/search/semantic-search)

### Sparse indexes

Sparse indexes store sparse vectors, which are a series of numbers that represent the words or phrases in a document. Sparse vectors have a very large number of dimensions, where only a small proportion of values are non-zero. The dimensions represent words from a dictionary, and the values represent the importance of these words in the document.

When you search a sparse index, Pinecone retrieves the sparse vectors that most exactly match the words or phrases in the query. Query terms are scored independently and then summed, with the most similar records scored highest. This is often called **lexical search** or **keyword search**.

Learn more:

* [Create a sparse index](/guides/index-data/create-an-index#create-a-sparse-index)
* [Upsert sparse vectors](/guides/index-data/upsert-data#upsert-sparse-vectors)
* [Lexical search](/guides/search/lexical-search)

<Tip>
  Semantic search can miss results based on exact keyword matches, while lexical search can miss results based on relationships. To lift these limitations, you can perform [hybrid search](/guides/search/hybrid-search).
</Tip>

#### Limitations

<Note>
  These limitations are subject to change during the public preview period.
</Note>

Sparse indexes have the following limitations:

* Max non-zero values per sparse vector: 1000
* Max upserts per second per sparse index: 10
* Max queries per second per sparse index: 100
* Max `top_k` value per query: 1000

  <Note>
    You may get fewer than `top_k` results if `top_k` is larger than the number of sparse vectors in your index that match your query. That is, any vectors where the dotproduct score is `0` will be discarded.
  </Note>
* Max query results size: 4MB

## Namespaces

Within an index, records are partitioned into namespaces, and all [upserts](/guides/index-data/upsert-data), [queries](/guides/search/search-overview), and other [data operations](/guides/index-data/upsert-data) always target one namespace. This has two main benefits:

* **Multitenancy:** When you need to isolate data between customers, you can use one namespace per customer and target each customer's writes and queries to their dedicated namespace. See [Implement multitenancy](/guides/index-data/implement-multitenancy) for end-to-end guidance.

* **Faster queries:** When you divide records into namespaces in a logical way, you speed up queries by ensuring only relevant records are scanned. The same applies to fetching records, listing record IDs, and other data operations.

Namespaces are created automatically during [upsert](/guides/index-data/upsert-data). If a namespace doesn't exist, it is created implicitly.

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=641c2aa9a3238bf70698c583097c1f29" width="1400" height="880" data-path="images/quickstart-upsert.png" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=5b394ed73cf8248f9a9ae8f9d3cdbd2d 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3bd0b45458ebbcab40605f149b5847d5 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=9c1e1b064228344b3caf4c0a1aa8ab82 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=d40dd481d2e7cc8882d766d6df59fcba 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=bf6be475e7bed3453299f6bbecd6aa54 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=46c9efa0b08b8ac3c907a121289c19f2 2500w" data-optimize="true" data-opv="2" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert-dark.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=14a3e6c2847455db0821ebbf9bd51df9" width="1400" height="880" data-path="images/quickstart-upsert-dark.png" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert-dark.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=229b97b3ea4581730afab68709201084 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert-dark.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=02fcdee17c689d31769c145fb86f259b 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert-dark.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=dd13a98f1154ffd8c4cc7cd4d37c0d33 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert-dark.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=b13689e423b344828452efcf91c737b4 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert-dark.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=319293ecf19a483936595aaebfb5cb31 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/quickstart-upsert-dark.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=78ad3d1499ae4d57ff9e9cd0a8e56093 2500w" data-optimize="true" data-opv="2" />

## Vector embedding

[Dense vectors](/guides/get-started/concepts#dense-vector) and [sparse vectors](/guides/get-started/concepts#sparse-vector) are the basic units of data in Pinecone and what Pinecone was specially designed to store and work with. Dense vectors represents the semantics of data such as text, images, and audio recordings, while sparse vectors represent documents or queries in a way that captures keyword information.

To transform data into vector format, you use an embedding model. You can either use Pinecone's integrated embedding models to convert your source data to vectors automatically, or you can use an external embedding model and bring your own vectors to Pinecone.

### Integrated embedding

1. [Create an index](/guides/index-data/create-an-index) that is integrated with one of Pinecone's [hosted embedding models](/guides/index-data/create-an-index#embedding-models).
2. [Upsert](/guides/index-data/upsert-data) your source text. Pinecone uses the integrated model to convert the text to vectors automatically.
3. [Search](/guides/search/search-overview) with a query text. Again, Pinecone uses the integrated model to convert the text to a vector automatically.

<Note>
  Indexes with integrated embedding do not support [updating](/guides/manage-data/update-data) or [importing](/guides/index-data/import-data) with text.
</Note>

### Bring your own vectors

1. Use an embedding model to convert your text to vectors. The model can be [hosted by Pinecone](/reference/api/latest/inference/generate-embeddings) or an external provider.
2. [Create an index](/guides/index-data/create-an-index) that matches the characteristics of the model.
3. [Upsert](/guides/index-data/upsert-data) your vectors directly.
4. Use the same external embedding model to convert a query to a vector.
5. [Search](/guides/search/search-overview) with your query vector directly.

## Data ingestion

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

There are two ways to ingest data into an index:

* [Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective way to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

* [Upserting](/guides/index-data/upsert-data) is intended for ongoing writes to an index. [Batch upserting](/guides/index-data/upsert-data#upsert-in-batches) can improve throughput performance and is a good option for larger numbers of records (up to 1000 per batch) if you cannot work around import's current limitations.

## Metadata

Every [record](/guides/get-started/concepts#record) in an index must contain an ID and a vector. In addition, you can include metadata key-value pairs to store additional information or context. When you query the index, you can then include a [metadata filter](/guides/search/filter-by-metadata) to limit the search to records matching a filter expression. Searches without metadata filters do not consider metadata and search the entire namespace.

### Metadata format

* Metadata fields must be key-value pairs in a flat JSON object. Nested JSON objects are not supported.
* Keys must be strings and must not start with a `$`.
* Values must be one of the following data types:
  * String
  * Integer (converted to a 64-bit floating point by Pinecone)
  * Floating point
  * Boolean (`true`, `false`)
  * List of strings
* Null metadata values aren't supported. Instead of setting a key to `null`, remove the key from the metadata payload.

**Examples**

<CodeGroup>
  ```json Valid metadata
  {
    "document_id": "document1",
    "document_title": "Introduction to Vector Databases",
    "chunk_number": 1,
    "chunk_text": "First chunk of the document content...",
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": ["85", "92"]
  }
  ```

  ```json Invalid metadata
  {
    "document": {       // Nested JSON objects are not supported
      "document_id": "document1",
      "document_title": "Introduction to Vector Databases",
    },
    "$chunk_number": 1, // Keys must not start with a `$`
    "chunk_text": null, // Null values are not supported
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": [85, 92]  // Lists of non-strings are not supported
  }
  ```
</CodeGroup>

### Metadata size

Pinecone supports 40KB of metadata per record.

### Metadata filter expressions

Pinecone's filtering language supports the following operators:

| Operator  | Function                                                                                                                           | Supported types         |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| `$eq`     | Matches {word_0} with metadata values that are equal to a specified value. Example: `{"genre": {"$eq": "documentary"}}`            | Number, string, boolean |
| `$ne`     | Matches {word_0} with metadata values that are not equal to a specified value. Example: `{"genre": {"$ne": "drama"}}`              | Number, string, boolean |
| `$gt`     | Matches {word_0} with metadata values that are greater than a specified value. Example: `{"year": {"$gt": 2019}}`                  | Number                  |
| `$gte`    | Matches {word_0} with metadata values that are greater than or equal to a specified value. Example:`{"year": {"$gte": 2020}}`      | Number                  |
| `$lt`     | Matches {word_0} with metadata values that are less than a specified value. Example: `{"year": {"$lt": 2020}}`                     | Number                  |
| `$lte`    | Matches {word_0} with metadata values that are less than or equal to a specified value. Example: `{"year": {"$lte": 2020}}`        | Number                  |
| `$in`     | Matches {word_0} with metadata values that are in a specified array. Example: `{"genre": {"$in": ["comedy", "documentary"]}}`      | String, number          |
| `$nin`    | Matches {word_0} with metadata values that are not in a specified array. Example: `{"genre": {"$nin": ["comedy", "documentary"]}}` | String, number          |
| `$exists` | Matches {word_0} with the specified metadata field. Example: `{"genre": {"$exists": true}}`                                        | Number, string, boolean |
| `$and`    | Joins query clauses with a logical `AND`. Example: `{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`             | -                       |
| `$or`     | Joins query clauses with a logical `OR`. Example: `{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`               | -                       |

<Note>
  Only `$and` and `$or` are allowed at the top level of the query expression.
</Note>

For example, the following has a `"genre"` metadata field with a list of strings:

```JSON JSON
{ "genre": ["comedy", "documentary"] }
```

This means `"genre"` takes on both values, and requests with the following filters will match:

```JSON JSON
{"genre":"comedy"}

{"genre": {"$in":["documentary","action"]}}

{"$and": [{"genre": "comedy"}, {"genre":"documentary"}]}
```

However, requests with the following filter will **not** match:

```JSON JSON
{ "$and": [{ "genre": "comedy" }, { "genre": "drama" }] }
```

Additionally, requests with the following filters will **not** match because they are invalid. They will result in a compilation error:

```json JSON
# INVALID QUERY:
{"genre": ["comedy", "documentary"]}
```

```json JSON
# INVALID QUERY:
{"genre": {"$eq": ["comedy", "documentary"]}}
```

# Create a serverless index

This page shows you how to create a dense or sparse serverless index.

* **Dense indexes** store dense vectors, which are numerical representations of the meaning and relationships of text, images, or other types of data. You use dense indexes for [semantic search](/guides/search/semantic-search) or in combination with sparse indexes for [hybrid search](/guides/search/hybrid-search).

* **Sparse indexes** store sparse vectors, which are numerical representations of the words or phrases in a document. You use sparse indexes for [lexical search](/guides/search/lexical-search), or in combination with dense indexes for [hybrid search](/guides/search/hybrid-search).

<Tip>
  You can create an index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless).
</Tip>

## Create a dense index

You can create a dense index with [integrated vector embedding](/guides/index-data/indexing-overview#integrated-embedding) or a dense index for storing vectors generated with an external embedding model.

### Integrated embedding

<Note>
  Indexes with integrated embedding do not support [updating](/guides/manage-data/update-data) or [importing](/guides/index-data/import-data) with text.
</Note>

If you want to upsert and search with source text and have Pinecone convert it to dense vectors automatically, [create a dense index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted embedding models](/guides/index-data/create-an-index#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the data for embedding.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_for_model) for details.

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "integrated-dense-py"

  if not pc.has_index(index_name):
      pc.create_index_for_model(
          name=index_name,
          cloud="aws",
          region="us-east-1",
          embed={
              "model":"llama-text-embed-v2",
              "field_map":{"text": "chunk_text"}
          }
      )
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndexForModel({
    name: 'integrated-dense-js',
    cloud: 'aws',
    region: 'us-east-1',
    embed: {
      model: 'llama-text-embed-v2',
      fieldMap: { text: 'chunk_text' },
    },
    waitUntilReady: true,
  });
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequest;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;
  import java.util.Map;

  public class CreateIntegratedIndex {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "integrated-dense-java";
          String region = "us-east-1";
          HashMap<String, String> fieldMap = new HashMap<>();
          fieldMap.put("text", "chunk_text");
          CreateIndexForModelRequestEmbed embed = new CreateIndexForModelRequestEmbed()
                  .model("llama-text-embed-v2")
                  .fieldMap(fieldMap);
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createIndexForModel(
                  indexName,
                  CreateIndexForModelRequest.CloudEnum.AWS,
                  region,
                  embed,
                  DeletionProtection.DISABLED,
                  tags
          );
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

    	indexName := "integrated-dense-go"
     	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
  		Name:   indexName,
  		Cloud:  pinecone.Aws,
  		Region: "us-east-1",
  		Embed: pinecone.CreateIndexForModelEmbed{
  			Model:    "llama-text-embed-v2",
  			FieldMap: map[string]interface{}{"text": "chunk_text"},
  		},
          DeletionProtection: &deletionProtection,
          Tags:   &pinecone.IndexTags{ "environment": "development" },
  	})
      if err != nil {
          log.Fatalf("Failed to create serverless integrated index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created serverless integrated index: %v", idx.Name)
      }
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var createIndexRequest = await pinecone.CreateIndexForModelAsync(
      new CreateIndexForModelRequest
      {
          Name = "integrated-dense-dotnet",
          Cloud = CreateIndexForModelRequestCloud.Aws,
          Region = "us-east-1",
          Embed = new CreateIndexForModelRequestEmbed
          {
              Model = "llama-text-embed-v2",
              FieldMap = new Dictionary<string, object?>() 
              { 
                  { "text", "chunk_text" } 
              }
          },
          DeletionProtection = DeletionProtection.Disabled,
          Tags = new Dictionary<string, string> 
          { 
              { "environment", "development" }
          }
      }
  );
  ```

  ```json curl
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes/create-for-model" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "name": "integrated-dense-curl",
          "cloud": "aws",
          "region": "us-east-1",
          "embed": {
            "model": "llama-text-embed-v2",
            "field_map": {
              "text": "chunk_text"
            }
          }
        }'
  ```
</CodeGroup>

### Bring your own vectors

If you use an external embedding model to convert your data to dense vectors, [create a dense index](/reference/api/latest/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `dense`.
* Specify the `dimension` and similarity `metric` of the vectors you'll store in the index. This should match the dimension and metric supported by your embedding model.
* Set `spec.cloud` and `spec.region` to the [cloud and region](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed. For Python, you also need to import the `ServerlessSpec` class.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_index) for details.

<CodeGroup>
  ```python Python
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "standard-dense-py"

  if not pc.has_index(index_name):
      pc.create_index(
          name=index_name,
          vector_type="dense",
          dimension=1536,
          metric="cosine",
          spec=ServerlessSpec(
              cloud="aws",
              region="us-east-1"
          ),
          deletion_protection="disabled",
          tags={
              "environment": "development"
          }
      )
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndex({
    name: 'standard-dense-js',
    vectorType: 'dense',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      }
    },
    deletionProtection: 'disabled',
    tags: { environment: 'development' }, 
  });
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;

  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "standard-dense-java";
          String cloud = "aws";
          String region = "us-east-1";
          String vectorType = "dense";
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createServerlessIndex(
              indexName,
              "cosine", 
              1536, 
              cloud,
              region,
              DeletionProtection.DISABLED, 
              tags, 
              vectorType
          );
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // Serverless index
    	indexName := "standard-dense-go"
  	vectorType := "dense"
      dimension := int32(1536)
      metric := pinecone.Cosine
  	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
          Name:               indexName,
          VectorType:         &vectorType,
          Dimension:          &dimension,
          Metric:             &metric,
          Cloud:              pinecone.Aws,
          Region:             "us-east-1",
          DeletionProtection: &deletionProtection,
          Tags:               &pinecone.IndexTags{ "environment": "development" },
      })
      if err != nil {
          log.Fatalf("Failed to create serverless index: %v", err)
      } else {
          fmt.Printf("Successfully created serverless index: %v", idx.Name)
      }
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var createIndexRequest = await pinecone.CreateIndexAsync(new CreateIndexRequest
  {
      Name = "standard-dense-dotnet",
      VectorType = VectorType.Dense,
      Dimension = 1536,
      Metric = MetricType.Cosine,
      Spec = new ServerlessIndexSpec
      {
          Serverless = new ServerlessSpec
          {
              Cloud = ServerlessSpecCloud.Aws,
              Region = "us-east-1"
          }
      },
      DeletionProtection = DeletionProtection.Disabled,
      Tags = new Dictionary<string, string> 
      {  
          { "environment", "development" }
      }
  });
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
           "name": "standard-dense-curl",
           "vector_type": "dense",
           "dimension": 1536,
           "metric": "cosine",
           "spec": {
              "serverless": {
                 "cloud": "aws",
                 "region": "us-east-1"
              }
           },
          "tags": {
              "environment": "development"
          },
           "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>

## Create a sparse index

You can create a sparse index with [integrated vector embedding](/guides/index-data/indexing-overview#integrated-embedding) or a sparse index for storing vectors generated with an external embedding model.

### Integrated embedding

If you want to upsert and search with source text and have Pinecone convert it to sparse vectors automatically, [create a sparse index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted sparse embedding models](/guides/index-data/create-an-index#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the text for embedding.
* If needed, `embed.read_parameters` and `embed.write_parameters` can be used to override the default model embedding behavior.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_for_model) for details.

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "integrated-sparse-py"

  if not pc.has_index(index_name):
      pc.create_index_for_model(
          name=index_name,
          cloud="aws",
          region="us-east-1",
          embed={
              "model":"pinecone-sparse-english-v0",
              "field_map":{"text": "chunk_text"}
          }
      )
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndexForModel({
    name: 'integrated-sparse-js',
    cloud: 'aws',
    region: 'us-east-1',
    embed: {
      model: 'pinecone-sparse-english-v0',
      fieldMap: { text: 'chunk_text' },
    },
    waitUntilReady: true,
  });
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequest;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;
  import java.util.Map;

  public class CreateIntegratedIndex {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "integrated-sparse-java";
          String region = "us-east-1";
          HashMap<String, String> fieldMap = new HashMap<>();
          fieldMap.put("text", "chunk_text");
          CreateIndexForModelRequestEmbed embed = new CreateIndexForModelRequestEmbed()
                  .model("pinecone-sparse-english-v0")
                  .fieldMap(fieldMap);
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createIndexForModel(
                  indexName,
                  CreateIndexForModelRequest.CloudEnum.AWS,
                  region,
                  embed,
                  DeletionProtection.DISABLED,
                  tags
          );
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

    	indexName := "integrated-sparse-go"
  	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
  		Name:   indexName,
  		Cloud:  pinecone.Aws,
  		Region: "us-east-1",
  		Embed: pinecone.CreateIndexForModelEmbed{
  			Model:    "pinecone-sparse-english-v0",
  			FieldMap: map[string]interface{}{"text": "chunk_text"},
  		},
          DeletionProtection: &deletionProtection,
          Tags:   &pinecone.IndexTags{ "environment": "development" },

  	})
      if err != nil {
          log.Fatalf("Failed to create serverless integrated index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created serverless integrated index: %v", idx.Name)
      }
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var createIndexRequest = await pinecone.CreateIndexForModelAsync(
      new CreateIndexForModelRequest
      {
          Name = "integrated-sparse-dotnet",
          Cloud = CreateIndexForModelRequestCloud.Aws,
          Region = "us-east-1",
          Embed = new CreateIndexForModelRequestEmbed
          {
              Model = "pinecone-sparse-english-v0",
              FieldMap = new Dictionary<string, object?>() 
              { 
                  { "text", "chunk_text" } 
              }
          },
          DeletionProtection = DeletionProtection.Disabled,
          Tags = new Dictionary<string, string> 
          { 
              { "environment", "development" }
          }
      }
  );
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes/create-for-model" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "name": "integrated-sparse-curl",
          "cloud": "aws",
          "region": "us-east-1",
          "embed": {
            "model": "pinecone-sparse-english-v0",
            "field_map": {
              "text": "chunk_text"
            }
          }
        }'
  ```
</CodeGroup>

### Bring your own vectors

If you use an external embedding model to convert your data to sparse vectors, [create a sparse index](/reference/api/latest/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `sparse`.
* Set the distance `metric` to `dotproduct`. Sparse indexes do not support other [distance metrics](/guides/index-data/indexing-overview#distance-metrics).
* Set `spec.cloud` and `spec.region` to the cloud and region where the index should be deployed.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_index) for details.

<CodeGroup>
  ```python Python
  from pinecone import Pinecone, ServerlessSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "standard-sparse-py"

  if not pc.has_index(index_name):
      pc.create_index(
          name=index_name,
          vector_type="sparse",
          metric="dotproduct",
          spec=ServerlessSpec(cloud="aws", region="us-east-1")
      )
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndex({
    name: 'standard-sparse-js',
    vectorType: 'sparse',
    metric: 'dotproduct',
    spec: {
      serverless: {
        cloud: 'aws',
        region: 'us-east-1'
      },
    },
  });
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.DeletionProtection;

  import java.util.*;

  public class SparseIndex {
      public static void main(String[] args) throws InterruptedException {
          // Instantiate Pinecone class
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Create sparse Index
          String indexName = "standard-sparse-java";
          String cloud = "aws";
          String region = "us-east-1";
          String vectorType = "sparse";
          Map<String, String> tags = new HashMap<>();
          tags.put("env", "test");
          pinecone.createSparseServelessIndex(indexName,
                  cloud,
                  region,
                  DeletionProtection.DISABLED,
                  tags,
                  vectorType);
      }
  }
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	indexName := "standard-sparse-go"
  	vectorType := "sparse"
  	metric := pinecone.Dotproduct
  	deletionProtection := pinecone.DeletionProtectionDisabled

  	idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
  		Name:               indexName,
  		Metric:             &metric,
  		VectorType:         &vectorType,
  		Cloud:              pinecone.Aws,
  		Region:             "us-east-1",
  		DeletionProtection: &deletionProtection,
  	})
  	if err != nil {
  		log.Fatalf("Failed to create serverless index: %v", err)
  	} else {
  		fmt.Printf("Successfully created serverless index: %v", idx.Name)
  	}
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var createIndexRequest = await pinecone.CreateIndexAsync(new CreateIndexRequest
  {
      Name = "standard-sparse-dotnet",
      VectorType = VectorType.Sparse,
      Metric = MetricType.Dotproduct,
      Spec = new ServerlessIndexSpec
      {
          Serverless = new ServerlessSpec
          {
              Cloud = ServerlessSpecCloud.Aws,
              Region = "us-east-1"
          }
      }
  });
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
           "name": "standard-sparse-curl",
           "vector_type": "sparse",
           "metric": "dotproduct",
           "spec": {
              "serverless": {
                 "cloud": "aws",
                 "region": "us-east-1"
              }
           }
        }'
  ```
</CodeGroup>

## Create an index from a backup

You can create a dense or sparse index from a backup. For more details, see [Restore an index](/guides/manage-data/restore-an-index).

## Metadata indexing

<Warning>
  This feature is in [early access](/release-notes/feature-availability) and available only on the `2025-10` version of the API.
</Warning>

Pinecone indexes all metadata fields by default. However, large amounts of metadata can cause slower [index building](/guides/get-started/database-architecture#index-builder) as well as slower [query execution](/guides/get-started/database-architecture#query-executors), particularly when data is not cached in a query executor's memory and local SSD and must be fetched from object storage.

To prevent performance issues due to excessive metadata, you can limit metadata indexing to the fields that you plan to use for [query filtering](/guides/search/filter-by-metadata).

### Set metadata indexing

You can set metadata indexing during index creation or [namespace creation](/reference/api/2025-10/data-plane/createnamespace):

* Index-level metadata indexing rules apply to all namespaces that don't have explicit metadata indexing rules.
* Namespace-level metadata indexing rules overrides index-level metadata indexing rules.

For example, let's say you want to store records that represent chunks of a document, with each record containing many metadata fields. Since you plan to use only a few of the metadata fields to filter queries, you would specify the metadata fields to index as follows.

<Warning>
  Metadata indexing cannot be changed after index or namespace creation.
</Warning>

<CodeGroup>
  ```shell Index-level metadata indexing
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
          "name": "example-index-metadata",
          "vector_type": "dense",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
              "serverless": {
                  "cloud": "aws",
                  "region": "us-east-1",
                  "schema": {
                      "fields": { 
                          "document_id": {"filterable": true},
                          "document_title": {"filterable": true},
                          "chunk_number": {"filterable": true},
                          "document_url": {"filterable": true},
                          "created_at": {"filterable": true}
                      }
                  }
              }
          },
          "deletion_protection": "disabled"
        }'
  ```

  ```shell Namespace-level metadata indexing
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
          "name": "example-namespace",
          "schema": {
  		  "fields": { 
              "document_id": {"filterable": true},
              "document_title": {"filterable": true},
              "chunk_number": {"filterable": true},
              "document_url": {"filterable": true},
              "created_at": {"filterable": true}
            }
          }
        }'
  ```
</CodeGroup>

### Check metadata indexing

To check which metadata fields are indexed, you can describe the index or namespace:

<CodeGroup>
  ```shell Describe index
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes/example-index-metadata" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-10"
  ```

  ```shell Describe namespace
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces/example-namespace" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-10"
  ```
</CodeGroup>

The response includes the `schema` object with the names of the metadata fields explicitly indexed during index or namespace creation.

<Note>
  The response does not include unindexed metadata fields or metadata fields indexed by default.
</Note>

<CodeGroup>
  ```json Describe index
  {
      "id": "294a122f-44e7-4a95-8d77-2d2d04200aa4",
      "vector_type": "dense",
      "name": "example-index",
      "metric": "cosine",
      "dimension": 1536,
      "status": {
          "ready": false,
          "state": "Initializing"
      },
      "host": "example-index-metadata-govk0nt.svc.aped-4627-b74a.pinecone.io",
      "spec": {
          "serverless": {
              "region": "us-east-1",
              "cloud": "aws",
              "read_capacity": {
                  "mode": "OnDemand",
                  "status": "Ready"
              },
              "schema": {
                  "fields": {
                      "document_id": {
                          "filterable": true
                      },
                      "document_title": {
                          "filterable": true
                      },
                      "created_at": {
                          "filterable": true
                      },
                      "chunk_number": {
                          "filterable": true
                      },
                      "document_url": {
                          "filterable": true
                      }
                  }
              }
          }
      },
      "deletion_protection": "disabled",
      "tags": null
  }
  ```

  ```json Describe namespace
  {
      "name": "example-namespace",
      "record_count": "20000",
      "schema": {
          "fields": {
              "document_title": {
                  "filterable": true
              },
              "document_url": {
                  "filterable": true
              },
              "chunk_number": {
                  "filterable": true
              },
              "document_id": {
                  "filterable": true
              },
              "created_at": {
                  "filterable": true
              }
          }
      }
  }
  ```
</CodeGroup>

## Index options

### Cloud regions

When creating an index, you must choose the cloud and region where you want the index to be hosted. The following table lists the available public clouds and regions and the plans that support them:

| Cloud   | Region                       | [Supported plans](https://www.pinecone.io/pricing/) | [Availability phase](/release-notes/feature-availability) |
| ------- | ---------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| `aws`   | `us-east-1` (Virginia)       | Starter, Standard, Enterprise                       | General availability                                      |
| `aws`   | `us-west-2` (Oregon)         | Standard, Enterprise                                | General availability                                      |
| `aws`   | `eu-west-1` (Ireland)        | Standard, Enterprise                                | General availability                                      |
| `gcp`   | `us-central1` (Iowa)         | Standard, Enterprise                                | General availability                                      |
| `gcp`   | `europe-west4` (Netherlands) | Standard, Enterprise                                | General availability                                      |
| `azure` | `eastus2` (Virginia)         | Standard, Enterprise                                | General availability                                      |

The cloud and region cannot be changed after a serverless index is created.

<Note>
  On the free Starter plan, you can create serverless indexes in the `us-east-1` region of AWS only. To create indexes in other regions, [upgrade your plan](/guides/organizations/manage-billing/upgrade-billing-plan).
</Note>

### Similarity metrics

When creating a dense index, you can choose from the following similarity metrics. For the most accurate results, choose the similarity metric used to train the embedding model for your vectors. For more information, see [Vector Similarity Explained](https://www.pinecone.io/learn/vector-similarity/).

<Note>[Sparse indexes](#sparse-indexes) must use the `dotproduct` metric.</Note>

<AccordionGroup>
  <Accordion title="Euclidean">
    Querying indexes with this metric returns a similarity score equal to the squared Euclidean distance between the result and query vectors.

    This metric calculates the square of the distance between two data points in a plane. It is one of the most commonly used distance metrics. For an example, see our [IT threat detection example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/it-threat-detection.ipynb).

    When you use `metric='euclidean'`, the most similar results are those with the **lowest similarity score**.
  </Accordion>

  <Accordion title="Cosine">
    This is often used to find similarities between different documents. The advantage is that the scores are normalized to \[-1,1] range. For an example, see our [generative question answering example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb).
  </Accordion>

  <Accordion title="Dotproduct">
    This is used to multiply two vectors. You can use it to tell us how similar the two vectors are. The more positive the answer is, the closer the two vectors are in terms of their directions. For an example, see our [semantic search example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb).
  </Accordion>
</AccordionGroup>

### Embedding models

[Dense vectors](/guides/get-started/concepts#dense-vector) and [sparse vectors](/guides/get-started/concepts#sparse-vector) are the basic units of data in Pinecone and what Pinecone was specially designed to store and work with. Dense vectors represents the semantics of data such as text, images, and audio recordings, while sparse vectors represent documents or queries in a way that captures keyword information.

To transform data into vector format, you use an embedding model. Pinecone hosts several embedding models so it's easy to manage your vector storage and search process on a single platform. You can use a hosted model to embed your data as an integrated part of upserting and querying, or you can use a hosted model to embed your data as a standalone operation.

The following embedding models are hosted by Pinecone.

<Note>
  To understand how cost is calculated for embedding, see [Embedding cost](/guides/manage-cost/understanding-cost#embedding). To get model details via the API, see [List models](/reference/api/latest/inference/list_models) and [Describe a model](/reference/api/latest/inference/describe_model).
</Note>

#### multilingual-e5-large

[`multilingual-e5-large`](/models/multilingual-e5-large) is an efficient dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs).

**Details**

* Vector type: Dense
* Modality: Text
* Dimension: 1024
* Recommended similarity metric: Cosine
* Max sequence length: 507 tokens
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits#embedding-tokens-per-minute-per-model) and [Embedding tokens per month](/reference/api/database-limits#embedding-tokens-per-month-per-model).

**Parameters**

The `multilingual-e5-large` model supports the following parameters:

| Parameter    | Type   | Required/Optional | Description                                                                                                                                                                                                                                    | Default |
| :----------- | :----- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `input_type` | string | Required          | The type of input data. Accepted values: `query` or `passage`.                                                                                                                                                                                 |         |
| `truncate`   | string | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END`   |

#### llama-text-embed-v2

[`llama-text-embed-v2`](/models/llama-text-embed-v2) is a high-performance dense embedding model optimized for text retrieval and ranking tasks. It is trained on a diverse range of text corpora and provides strong performance on longer passages and structured documents.

**Details**

* Vector type: Dense
* Modality: Text
* Dimension: 1024 (default), 2048, 768, 512, 384
* Recommended similarity metric: Cosine
* Max sequence length: 2048 tokens
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits#embedding-tokens-per-minute-per-model) and [Embedding tokens per month](/reference/api/database-limits#embedding-tokens-per-month-per-model).

**Parameters**

The `llama-text-embed-v2` model supports the following parameters:

| Parameter    | Type    | Required/Optional | Description                                                                                                                                                                                                                                    | Default |
| :----------- | :------ | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `input_type` | string  | Required          | The type of input data. Accepted values: `query` or `passage`.                                                                                                                                                                                 |         |
| `truncate`   | string  | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END`   |
| `dimension`  | integer | Optional          | Dimension of the vector to return.                                                                                                                                                                                                             | 1024    |

#### pinecone-sparse-english-v0

[`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) is a sparse embedding model for converting text to [sparse vectors](/guides/get-started/concepts#sparse-vector) for keyword or hybrid semantic/keyword search. Built on the innovations of the [DeepImpact architecture](https://arxiv.org/pdf/2104.12016), the model directly estimates the lexical importance of tokens by leveraging their context, unlike traditional retrieval models like BM25, which rely solely on term frequency.

**Details**

* Vector type: Sparse
* Modality: Text
* Recommended similarity metric: Dotproduct
* Max sequence length: 512 or 2048
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits#embedding-tokens-per-minute-per-model) and [Embedding tokens per month](/reference/api/database-limits#embedding-tokens-per-month-per-model).

**Parameters**

The `pinecone-sparse-english-v0` model supports the following parameters:

| Parameter                 | Type    | Required/Optional | Description                                                                                                                                                                                                                                                                    | Default |
| :------------------------ | :------ | :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `input_type`              | string  | Required          | The type of input data. Accepted values: `query` or `passage`.                                                                                                                                                                                                                 |         |
| `max_tokens_per_sequence` | integer | Optional          | Maximum number of tokens to embed. Accepted values: `512` or `2048`.                                                                                                                                                                                                           | `512`   |
| `truncate`                | string  | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the the `max_tokens_per_sequence` limit. `NONE` returns an error when the input exceeds the `max_tokens_per_sequence` limit. | `END`   |
| `return_tokens`           | boolean | Optional          | Whether to return the string tokens.                                                                                                                                                                                                                                           | `false` |

# Data modeling

This page shows you how to model your data for efficient ingestion, retrieval, and management in Pinecone.

## Record format

<Tabs>
  <Tab title="Text">
    When you upsert raw text for Pinecone to convert to vectors automatically, each record consists of the following:

    * **ID**: A unique string identifier for the record.
    * **Text**: The raw text for Pinecone to convert to a dense vector for [semantic search](/guides/search/semantic-search) or a sparse vector for [lexical search](/guides/search/lexical-search), depending on the [embedding model](/guides/index-data/create-an-index#embedding-models) integrated with the index. This field name must match the `embed.field_map` defined in the index.
    * **Metadata** (optional): All additional fields are stored as record metadata. You can filter by metadata when searching or deleting records.

    <Note>
      Upserting raw text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#vector-embedding).
    </Note>

    Example:

    ```json
    {
      "_id": "document1#chunk1", 
      "chunk_text": "First chunk of the document content...", // Text to convert to a vector. 
      "document_id": "document1", // This and subsequent fields stored as metadata. 
      "document_title": "Introduction to Vector Databases",
      "chunk_number": 1,
      "document_url": "https://example.com/docs/document1", 
      "created_at": "2024-01-15",
      "document_type": "tutorial"
    }
    ```
  </Tab>

  <Tab title="Vectors">
    When you upsert pre-generated vectors, each record consists of the following:

    * **ID**: A unique string identifier for the record.
    * **Vector**: A dense vector for [semantic search](/guides/search/semantic-search), a sparse vector for [lexical search](/guides/search/lexical-search), or both for [hybrid search](/guides/search/hybrid-search) using a single hybrid index.
    * **Metadata** (optional):  A flat JSON document containing key-value pairs with additional information (nested objects are not supported). You can filter by metadata when searching or deleting records.

    <Note>
      When importing data from object storage, records must be in Parquet format. For more details, see [Import data](/guides/index-data/import-data#prepare-your-data).
    </Note>

    Example:

    <CodeGroup>
      ```json Dense
      {
        "id": "document1#chunk1", 
        "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
        "metadata": {
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "chunk_text": "First chunk of the document content...",
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        }
      }
      ```

      ```json Sparse
      {
        "id": "document1#chunk1", 
        "sparse_values": {
          "values": [1.7958984, 0.41577148, ..., 4.4414062, 3.3554688],
          "indices": [822745112, 1009084850, ..., 3517203014, 3590924191]
        },
        "metadata": {
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "chunk_text": "First chunk of the document content...",
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        }
      }
      ```

      ```json Hybrid
      {
        "id": "document1#chunk1", 
        "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
        "sparse_values": {
          "values": [1.7958984, 0.41577148, ..., 4.4414062, 3.3554688],
          "indices": [822745112, 1009084850, ..., 3517203014, 3590924191]
        },
        "metadata": {
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "chunk_text": "First chunk of the document content...",
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        }
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Use structured IDs

Use a structured, human-readable format for record IDs, including ID prefixes that reflect the type of data you're storing, for example:

* **Document chunks**: `document_id#chunk_number`
* **User data**: `user_id#data_type#item_id`
* **Multi-tenant data**: `tenant_id#document_id#chunk_id`

Choose a delimiter for your ID prefixes that won't appear elsewhere in your IDs. Common patterns include:

* `document1#chunk1` - Using hash delimiter
* `document1_chunk1` - Using underscore delimiter
* `document1:chunk1` - Using colon delimiter

Structuring IDs in this way provides several advantages:

* **Efficiency**: Applications can quickly identify which record it should operate on.
* **Clarity**: Developers can easily understand what they're looking at when examining records.
* **Flexibility**: ID prefixes enable list operations for fetching and updating records.

## Include metadata

Include [metadata key-value pairs](/guides/index-data/indexing-overview#metadata) that support your application's key operations, for example:

* **Enable query-time filtering**: Add fields for time ranges, categories, or other criteria for [filtering searches for increased accuracy and relevance](/guides/search/filter-by-metadata).
* **Link related chunks**: Use fields like `document_id` and `chunk_number` to keep track of related records and enable efficient [chunk deletion](#delete-chunks) and [document updates](#update-an-entire-document).
* **Link back to original data**: Include `chunk_text` or `document_url` for traceability and user display.

Metadata keys must be strings, and metadata values must be one of the following data types:

* String
* Number (integer or floating point, gets converted to a 64-bit floating point)
* Boolean (true, false)
* List of strings

<Note>
  Pinecone supports 40 KB of metadata per record.
</Note>

## Example

This example demonstrates how to manage document chunks in Pinecone using structured IDs and comprehensive metadata. It covers the complete lifecycle of chunked documents: upserting, searching, fetching, updating, and deleting chunks, and updating an entire document.

### Upsert chunks

When [upserting](/guides/index-data/upsert-data) documents that have been split into chunks, combine structured IDs with comprehensive metadata:

<Tabs>
  <Tab title="Upsert text">
    <Note>
      Upserting raw text is supported only for [indexes with integrated embedding](/guides/index-data/create-an-index#integrated-embedding).
    </Note>

    ```python Python
    from pinecone.grpc import PineconeGRPC as Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    index.upsert_records(
      "example-namespace",
      [
        {
          "_id": "document1#chunk1", 
          "chunk_text": "First chunk of the document content...",
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 1,
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        },
        {
          "_id": "document1#chunk2", 
          "chunk_text": "Second chunk of the document content...",
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases", 
          "chunk_number": 2,
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        },
        {
          "_id": "document1#chunk3", 
          "chunk_text": "Third chunk of the document content...",
          "document_id": "document1",
          "document_title": "Introduction to Vector Databases",
          "chunk_number": 3, 
          "document_url": "https://example.com/docs/document1",
          "created_at": "2024-01-15",
          "document_type": "tutorial"
        },
      ]
    )
    ```
  </Tab>

  <Tab title="Upsert vectors">
    ```python Python
    from pinecone.grpc import PineconeGRPC as Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    index.upsert(
      namespace="example-namespace",
      vectors=[
        {
          "id": "document1#chunk1", 
          "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
          "metadata": {
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases",
            "chunk_number": 1,
            "chunk_text": "First chunk of the document content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "document_type": "tutorial"
          }
        },
        {
          "id": "document1#chunk2", 
          "values": [-0.0412445068359375, 0.028839111328125, ..., 0.01953125, -0.0174560546875],
          "metadata": {
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases", 
            "chunk_number": 2,
            "chunk_text": "Second chunk of the document content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "document_type": "tutorial"
          }
        },
        {
          "id": "document1#chunk3", 
          "values": [0.0512237548828125, 0.041656494140625, ..., 0.02130126953125, -0.0394287109375],
          "metadata": {
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases",
            "chunk_number": 3, 
            "chunk_text": "Third chunk of the document content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "document_type": "tutorial"
          }
        }
      ]
    )
    ```
  </Tab>
</Tabs>

### Search chunks

To search the chunks of a document, use a [metadata filter expression](/guides/search/filter-by-metadata#metadata-filter-expressions) that limits the search appropriately:

<Tabs>
  <Tab title="Search with text">
    <Note>
      Searching with text is supported only for [indexes with integrated embedding](/guides/index-data/create-an-index#integrated-embedding).
    </Note>

    ```python Python
    from pinecone import Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    filtered_results = index.search(
        namespace="example-namespace", 
        query={
            "inputs": {"text": "What is a vector database?"}, 
            "top_k": 3,
            "filter": {"document_id": "document1"}
        },
        fields=["chunk_text"]
    )

    print(filtered_results)
    ```
  </Tab>

  <Tab title="Search with a vector">
    ```python Python
    from pinecone.grpc import PineconeGRPC as Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    filtered_results = index.query(
        namespace="example-namespace",
        vector=[0.0236663818359375,-0.032989501953125, ..., -0.01041412353515625,0.0086669921875], 
        top_k=3,
        filter={
            "document_id": {"$eq": "document1"}
        },
        include_metadata=True,
        include_values=False
    )

    print(filtered_results)
    ```
  </Tab>
</Tabs>

### Fetch chunks

To retrieve all chunks for a specific document, first [list the record IDs](/guides/manage-data/list-record-ids) using the document prefix, and then [fetch](/guides/manage-data/fetch-data) the complete records:

```python Python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

# List all chunks for document1 using ID prefix
chunk_ids = []
for record_id in index.list(prefix='document1#', namespace='example-namespace'):
    chunk_ids.append(record_id)

print(f"Found {len(chunk_ids)} chunks for document1")

# Fetch the complete records by ID
if chunk_ids:
    records = index.fetch(ids=chunk_ids, namespace='example-namespace')
    
    for record_id, record_data in records['vectors'].items():
        print(f"Chunk ID: {record_id}")
        print(f"Chunk text: {record_data['metadata']['chunk_text']}")
        # Process the vector values and metadata as needed
```

<Note>
  Pinecone is [eventually consistent](/guides/index-data/check-data-freshness), so it's possible that a write (upsert, update, or delete) followed immediately by a read (query, list, or fetch) may not return the latest version of the data. If your use case requires retrieving data immediately, consider implementing a small delay or retry logic after writes.
</Note>

### Update chunks

To [update](/guides/manage-data/update-data) specific chunks within a document, first list the chunk IDs, and then update individual records:

```python Python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

# List all chunks for document1
chunk_ids = []
for record_id in index.list(prefix='document1#', namespace='example-namespace'):
    chunk_ids.append(record_id)

# Update specific chunks (e.g., update chunk 2)
if 'document1#chunk2' in chunk_ids:
    index.update(
        id='document1#chunk2',
        values=[<new dense vector>],
        set_metadata={
            "document_id": "document1",
            "document_title": "Introduction to Vector Databases - Revised",
            "chunk_number": 2,
            "chunk_text": "Updated second chunk content...",
            "document_url": "https://example.com/docs/document1",
            "created_at": "2024-01-15",
            "updated_at": "2024-02-15",
            "document_type": "tutorial"
        },
        namespace='example-namespace'
    )
    print("Updated chunk 2 successfully")
```

### Delete chunks

To [delete](/guides/manage-data/delete-data#delete-records-by-metadata) chunks of a document, use a [metadata filter expression](/guides/search/filter-by-metadata#metadata-filter-expressions) that limits the deletion appropriately:

```python Python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

# Delete chunks 1 and 3
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"},
        "chunk_number": {"$in": [1, 3]}
    }
)

# Delete all chunks for a document
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"}
    }
)
```

### Update an entire document

When the amount of chunks or ordering of chunks for a document changes, the recommended approach is to first [delete all chunks using a metadata filter](/guides/manage-data/delete-data#delete-records-by-metadata), and then [upsert](/guides/index-data/upsert-data) the new chunks:

```python Python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

# Step 1: Delete all existing chunks for the document
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"}
    }
)

print("Deleted existing chunks for document1")

# Step 2: Upsert the updated document chunks
index.upsert(
  namespace="example-namespace", 
  vectors=[
    {
      "id": "document1#chunk1",
      "values": [<updated dense vector>],
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases - Updated Edition",
        "chunk_number": 1,
        "chunk_text": "Updated first chunk with new content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-02-15",
        "document_type": "tutorial",
        "version": "2.0"
      }
    },
    {
      "id": "document1#chunk2",
      "values": [<updated dense vector>],
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases - Updated Edition",
        "chunk_number": 2,
        "chunk_text": "Updated second chunk with new content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-02-15",
        "document_type": "tutorial",
        "version": "2.0"
      }
    }
    # Add more chunks as needed for the updated document
  ]
)

print("Successfully updated document1 with new chunks")
```

## Data freshness

Pinecone is [eventually consistent](/guides/index-data/check-data-freshness), so it's possible that a write (upsert, update, or delete) followed immediately by a read (query, list, or fetch) may not return the latest version of the data. If your use case requires retrieving data immediately, consider implementing a small delay or retry logic after writes.

# Data ingestion overview

To ingest data into an index, you can [import from object storage](#import-from-object-storage) or use the [upsert](#upsert) operation.

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

## Upsert

For ongoing ingestion into an index, either one record at a time or in batches, use the [upsert](/guides/index-data/upsert-data) operation. [Batch uperting](/guides/index-data/upsert-data#upsert-in-batches) can improve throughput performance and is a good option for larger numbers of records if you cannot work around import's current [limitations](/guides/index-data/import-data#import-limits).

## Ingestion cost

* To understand how cost is calculated for imports, see [Import cost](/guides/manage-cost/understanding-cost#imports).
* To understand how cost is calculated for upserts, see [Upsert cost](/guides/manage-cost/understanding-cost#upsert).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).

# Upsert records

This page shows you how to upsert records into a namespace in an index. [Namespaces](/guides/index-data/indexing-overview#namespaces) let you partition records within an index and are essential for [implementing multitenancy](/guides/index-data/implement-multitenancy) when you need to isolate the data of each customer/user.

If a record ID already exists, upserting overwrites the entire record. To change only part of a record, [update ](/guides/manage-data/update-data) the record.

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

## Upsert dense vectors

<Tabs>
  <Tab title="Upsert text">
    <Note>
      Upserting text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
    </Note>

    To upsert source text into a [dense index with integrated embedding](/guides/index-data/create-an-index#create-a-dense-index), use the [`upsert_records`](/reference/api/latest/data-plane/upsert_records) operation. Pinecone converts the text to dense vectors automatically using the hosted dense embedding model associated with the index.

    * Specify the [`namespace`](/guides/index-data/indexing-overview#namespaces) to upsert into. If the namespace doesn't exist, it is created. To use the default namespace, set the namespace to `"__default__"`.
    * Format your input data as records, each with the following:
      * An `_id` field with a unique record identifier for the index namespace. `id` can be used as an alias for `_id`.
      * A field with the source text to convert to a vector. This field must match the `field_map` specified in the index.
      * Additional fields are stored as record [metadata](/guides/index-data/indexing-overview#metadata) and can be returned in search results or used to [filter search results](/guides/search/filter-by-metadata).

    For example, the following code converts the sentences in the `chunk_text` fields to dense vectors and then upserts them into `example-namespace` in an example index. The additional `category` field is stored as metadata.

    <CodeGroup>
      ```python Python
      from pinecone import Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")

      # To get the unique host for an index, 
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      index = pc.Index(host="INDEX_HOST")

      # Upsert records into a namespace
      # `chunk_text` fields are converted to dense vectors
      # `category` fields are stored as metadata
      index.upsert_records(
          "example-namespace",
          [
              {
                  "_id": "rec1",
                  "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
                  "category": "digestive system", 
              },
              {
                  "_id": "rec2",
                  "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
                  "category": "cultivation",
              },
              {
                  "_id": "rec3",
                  "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
                  "category": "immune system",
              },
              {
                  "_id": "rec4",
                  "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
                  "category": "endocrine system",
              },
          ]
      ) 
      ```

      ```javascript JavaScript
      import { Pinecone } from '@pinecone-database/pinecone'

      const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

      // Upsert records into a namespace
      // `chunk_text` fields are converted to dense vectors
      // `category` is stored as metadata
      await namespace.upsertRecords([
              {
                  "_id": "rec1",
                  "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
                  "category": "digestive system", 
              },
              {
                  "_id": "rec2",
                  "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
                  "category": "cultivation",
              },
              {
                  "_id": "rec3",
                  "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
                  "category": "immune system",
              },
              {
                  "_id": "rec4",
                  "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
                  "category": "endocrine system",
              }
      ]);
      ```

      ```java Java
      import io.pinecone.clients.Index;
      import io.pinecone.configs.PineconeConfig;
      import io.pinecone.configs.PineconeConnection;
      import org.openapitools.db_data.client.ApiException;

      import java.util.*;

      public class UpsertText {
          public static void main(String[] args) throws ApiException {
              PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
              config.setHost("INDEX_HOST");
              PineconeConnection connection = new PineconeConnection(config);

              Index index = new Index(config, connection, "integrated-dense-java");
              ArrayList<Map<String, String>> upsertRecords = new ArrayList<>();

              HashMap<String, String> record1 = new HashMap<>();
              record1.put("_id", "rec1");
              record1.put("category", "digestive system");
              record1.put("chunk_text", "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.");

              HashMap<String, String> record2 = new HashMap<>();
              record2.put("_id", "rec2");
              record2.put("category", "cultivation");
              record2.put("chunk_text", "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.");

              HashMap<String, String> record3 = new HashMap<>();
              record3.put("_id", "rec3");
              record3.put("category", "immune system");
              record3.put("chunk_text", "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.");

              HashMap<String, String> record4 = new HashMap<>();
              record4.put("_id", "rec4");
              record4.put("category", "endocrine system");
              record4.put("chunk_text", "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.");

              upsertRecords.add(record1);
              upsertRecords.add(record2);
              upsertRecords.add(record3);
              upsertRecords.add(record4);

              index.upsertRecords("example-namespace", upsertRecords);
          }
      }
      ```

      ```go Go
      package main

      import (
          "context"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
          if err != nil {
              log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      	  }

          // Upsert records into a namespace
          // `chunk_text` fields are converted to dense vectors
          // `category` is stored as metadata
      	records := []*pinecone.IntegratedRecord{
              {
                  "_id": "rec1",
                  "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
                  "category": "digestive system", 
              },
              {
                  "_id": "rec2",
                  "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
                  "category": "cultivation",
              },
              {
                  "_id": "rec3",
                  "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
                  "category": "immune system",
              },
              {
                  "_id": "rec4",
                  "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
                  "category": "endocrine system",
              },
      	}

      	err = idxConnection.UpsertRecords(ctx, records)
      	if err != nil {
      		log.Fatalf("Failed to upsert vectors: %v", err)
      	}
      }
      ```

      ```csharp C#
      using Pinecone;

      var pinecone = new PineconeClient("YOUR_API_KEY");

      var index = pinecone.Index(host: "INDEX_HOST");

      await index.UpsertRecordsAsync(
          "example-namespace",
          [
              new UpsertRecord
              {
                  Id = "rec1",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                      ["category"] = "technology",
                      ["quarter"] = "Q3",
                  },
              },
              new UpsertRecord
              {
                  Id = "rec2",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                      ["category"] = "technology",
                      ["quarter"] = "Q4",
                  },
              },  
              new UpsertRecord
              {
                  Id = "rec3",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                      ["category"] = "technology",
                      ["quarter"] = "Q4",
                  },
              },
              new UpsertRecord
              {
                  Id = "rec4",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                      ["category"] = "technology",
                      ["quarter"] = "Q3",
                  },
              },
          ]
      );
      ```

      ```shell curl
      # To get the unique host for an index,
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      INDEX_HOST="INDEX_HOST"
      NAMESPACE="YOUR_NAMESPACE"
      PINECONE_API_KEY="YOUR_API_KEY"

      # Upsert records into a namespace
      # `chunk_text` fields are converted to dense vectors
      # `category` is stored as metadata
      curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/upsert" \
        -H "Content-Type: application/x-ndjson" \
        -H "Api-Key: $PINECONE_API_KEY" \
        -H "X-Pinecone-API-Version: 2025-04" \
        -d '{"_id": "rec1", "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.", "category": "digestive system"}
            {"_id": "rec2", "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.", "category": "cultivation"}
            {"_id": "rec3", "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.", "category": "immune system"}
            {"_id": "rec4", "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.", "category": "endocrine system"}'
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Upsert vectors">
    To upsert dense vectors into a [dense index](/guides/index-data/create-an-index#create-a-dense-index), use the [`upsert`](/reference/api/latest/data-plane/upsert) operation as follows:

    * Specify the [`namespace`](/guides/index-data/indexing-overview#namespaces) to upsert into. If the namespace doesn't exist, it is created. To use the default namespace, set the namespace to `"__default__"`.
    * Format your input data as records, each with the following:
      * An `id` field with a unique record identifier for the index namespace.
      * A `values` field with the dense vector values.
      * Optionally, a `metadata` field with [key-value pairs](/guides/index-data/indexing-overview#metadata) to store additional information or context. When you query the index, you can use metadata to [filter search results](/guides/search/filter-by-metadata).

    <CodeGroup>
      ```Python Python
      from pinecone.grpc import PineconeGRPC as Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")

      # To get the unique host for an index, 
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      index = pc.Index(host="INDEX_HOST")

      index.upsert(
        vectors=[
          {
            "id": "A", 
            "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
            "metadata": {"genre": "comedy", "year": 2020}
          },
          {
            "id": "B", 
            "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
            "metadata": {"genre": "documentary", "year": 2019}
          },
          {
            "id": "C", 
            "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
            "metadata": {"genre": "comedy", "year": 2019}
          },
          {
            "id": "D", 
            "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
            "metadata": {"genre": "drama"}
          }
        ],
        namespace="example-namespace"
      )
      ```

      ```javascript JavaScript
      import { Pinecone } from '@pinecone-database/pinecone'

      const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const index = pc.index("INDEX_NAME", "INDEX_HOST")

      const records = [
          {
            id: 'A',
            values: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            metadata: { genre: "comedy", year: 2020 },
          },
          {
            id: 'B',
            values: [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
            metadata: { genre: "documentary", year: 2019 },
          },
          {
            id: 'C',
            values: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
            metadata: { genre: "comedy", year: 2019 },
          },
          {
            id: 'D',
            values: [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
            metadata: { genre: "drama" },
          }
      ]

      await index.('example-namespace').upsert(records);
      ```

      ```java Java
      import com.google.protobuf.Struct;
      import com.google.protobuf.Value;
      import io.pinecone.clients.Index;
      import io.pinecone.configs.PineconeConfig;
      import io.pinecone.configs.PineconeConnection;

      import java.util.Arrays;
      import java.util.List;

      public class UpsertExample {
          public static void main(String[] args) {
              PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
              // To get the unique host for an index, 
              // see https://docs.pinecone.io/guides/manage-data/target-an-index
              config.setHost("INDEX_HOST");
              PineconeConnection connection = new PineconeConnection(config);
              Index index = new Index(connection, "INDEX_NAME");
              List<Float> values1 = Arrays.asList(0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f);
              List<Float> values2 = Arrays.asList(0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f);
              List<Float> values3 = Arrays.asList(0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f);
              List<Float> values4 = Arrays.asList(0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f);
              Struct metaData1 = Struct.newBuilder()
                      .putFields("genre", Value.newBuilder().setStringValue("comedy").build())
                      .putFields("year", Value.newBuilder().setNumberValue(2020).build())
                      .build();
              Struct metaData2 = Struct.newBuilder()
                      .putFields("genre", Value.newBuilder().setStringValue("documentary").build())
                      .putFields("year", Value.newBuilder().setNumberValue(2019).build())
                      .build();
              Struct metaData3 = Struct.newBuilder()
                      .putFields("genre", Value.newBuilder().setStringValue("comedy").build())
                      .putFields("year", Value.newBuilder().setNumberValue(2019).build())
                      .build();
              Struct metaData4 = Struct.newBuilder()
                      .putFields("genre", Value.newBuilder().setStringValue("drama").build())
                      .build();

              index.upsert("A", values1, null, null, metaData1, 'example-namespace');
              index.upsert("B", values2, null, null, metaData2, 'example-namespace');
              index.upsert("C", values3, null, null, metaData3, 'example-namespace');
              index.upsert("D", values4, null, null, metaData4, 'example-namespace');
          }
      }
      ```

      ```go Go
      package main

      import (
          "context"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
          "google.golang.org/protobuf/types/known/structpb"
      )

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
          if err != nil {
              log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      	  }

          metadataMap1 := map[string]interface{}{
              "genre": "comedy",
              "year": 2020,
          }

          metadata1, err := structpb.NewStruct(metadataMap1)
          if err != nil {
              log.Fatalf("Failed to create metadata map: %v", err)
          }

          metadataMap2 := map[string]interface{}{
              "genre": "documentary",
              "year": 2019,
          }

          metadata2, err := structpb.NewStruct(metadataMap2)
          if err != nil {
              log.Fatalf("Failed to create metadata map: %v", err)
          }

          metadataMap3 := map[string]interface{}{
              "genre": "comedy",
              "year": 2019,
          }

          metadata3, err := structpb.NewStruct(metadataMap3)
          if err != nil {
              log.Fatalf("Failed to create metadata map: %v", err)
          }

          metadataMap4 := map[string]interface{}{
              "genre": "drama",
          }

          metadata4, err := structpb.NewStruct(metadataMap4)
          if err != nil {
              log.Fatalf("Failed to create metadata map: %v", err)
          }

          vectors := []*pinecone.Vector{
              {
                  Id:     "A",
                  Values: []float32{0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1},
                  Metadata: metadata1,
              },
              {
                  Id:     "B",
                  Values: []float32{0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2},
                  Metadata: metadata2,
              },
              {
                  Id:     "C",
                  Values: []float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3},
                  Metadata: metadata3,
              },   
              {
                  Id:     "D",
                  Values: []float32{0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4},
                  Metadata: metadata4,
              },   
          }

          count, err := idxConnection.UpsertVectors(ctx, vectors)
          if err != nil {
              log.Fatalf("Failed to upsert vectors: %v", err)
          } else {
              fmt.Printf("Successfully upserted %d vector(s)!\n", count)
          }
      }
      ```

      ```csharp C#
      using Pinecone;

      var pinecone = new PineconeClient("YOUR_API_KEY");

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      var index = pinecone.Index(host: "INDEX_HOST");

      var upsertResponse = await index.UpsertAsync(new UpsertRequest {
          Vectors = new[]
          {
              new Vector
              {
                  Id = "A",
                  Values = new[] { 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f },
                  Metadata = new Metadata {
                      ["genre"] = new("comedy"),
                      ["year"] = new(2020),
                  },
              },
              new Vector
              {
                  Id = "B",
                  Values = new[] { 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f },
                  Metadata = new Metadata {
                      ["genre"] = new("documentary"),
                      ["year"] = new(2019),
                  },
              },
              new Vector
              {
                  Id = "C",
                  Values = new[] { 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f },
                  Metadata = new Metadata {
                      ["genre"] = new("comedy"),
                      ["year"] = new(2019),
                  },
              },
              new Vector
              {
                  Id = "D",
                  Values = new[] { 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f },
                  Metadata = new Metadata {
                      ["genre"] = new("drama"),
                  },
              }
          },
          Namespace = "example-namespace",
      });
      ```

      ```bash curl
      # To get the unique host for an index,
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      PINECONE_API_KEY="YOUR_API_KEY"
      INDEX_HOST="INDEX_HOST"

      curl "https://$INDEX_HOST/vectors/upsert" \
        -H "Api-Key: $PINECONE_API_KEY" \
        -H 'Content-Type: application/json' \
        -H "X-Pinecone-API-Version: 2025-04" \
        -d '{
          "vectors": [
            {
              "id": "A",
              "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
              "metadata": {"genre": "comedy", "year": 2020}
            },
            {
              "id": "B",
              "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
              "metadata": {"genre": "documentary", "year": 2019}
            },
            {
              "id": "C",
              "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
              "metadata": {"genre": "comedy", "year": 2019}
            },
            {
              "id": "D",
              "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
              "metadata": {"genre": "drama"}
            }
          ],
          "namespace": "example-namespace"
        }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Upsert sparse vectors

<Tabs>
  <Tab title="Upsert text">
    <Note>
      Upserting text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
    </Note>

    To upsert source text into a [sparse index with integrated embedding](/guides/index-data/create-an-index#create-a-sparse-index), use the [`upsert_records`](/reference/api/latest/data-plane/upsert_records) operation. Pinecone converts the text to sparse vectors automatically using the hosted sparse embedding model associated with the index.

    * Specify the [`namespace`](/guides/index-data/indexing-overview#namespaces) to upsert into. If the namespace doesn't exist, it is created. To use the default namespace, set the namespace to `"__default__"`.
    * Format your input data as records, each with the following:
      * An `_id` field with a unique record identifier for the index namespace. `id` can be used as an alias for `_id`.
      * A field with the source text to convert to a vector. This field must match the `field_map` specified in the index.
      * Additional fields are stored as record [metadata](/guides/index-data/indexing-overview#metadata) and can be returned in search results or used to [filter search results](/guides/search/filter-by-metadata).

    For example, the following code converts the sentences in the `chunk_text` fields to sparse vectors and then upserts them into `example-namespace` in an example index. The additional `category` and `quarter` fields are stored as metadata.

    <CodeGroup>
      ```python Python
      from pinecone import Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")

      # To get the unique host for an index, 
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      index = pc.Index(host="INDEX_HOST")

      # Upsert records into a namespace
      # `chunk_text` fields are converted to sparse vectors
      # `category` and `quarter` fields are stored as metadata
      index.upsert_records(
          "example-namespace",
          [
              { 
                  "_id": "vec1", 
                  "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.", 
                  "category": "technology",
                  "quarter": "Q3"
              },
              { 
                  "_id": "vec2", 
                  "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.", 
                  "category": "technology",
                  "quarter": "Q4"
              },
              { 
                  "_id": "vec3", 
                  "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
                  "category": "technology",
                  "quarter": "Q3"
              },
              { 
                  "_id": "vec4", 
                  "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.", 
                  "category": "technology",
                  "quarter": "Q4"
              }
          ]
      )

      time.sleep(10) # Wait for the upserted vectors to be indexed
      ```

      ```javascript JavaScript
      import { Pinecone } from '@pinecone-database/pinecone'

      const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

      // Upsert records into a namespace
      // `chunk_text` fields are converted to sparse vectors
      // `category` and `quarter` fields are stored as metadata
      await namespace.upsertRecords([
          { 
              "_id": "vec1", 
              "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.", 
              "category": "technology",
              "quarter": "Q3"
          },
          { 
              "_id": "vec2", 
              "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.", 
              "category": "technology",
              "quarter": "Q4"
          },
          { 
              "_id": "vec3", 
              "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
              "category": "technology",
              "quarter": "Q3"
          },
          { 
              "_id": "vec4", 
              "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.", 
              "category": "technology",
              "quarter": "Q4"
          }
      ]);
      ```

      ```java Java
      import io.pinecone.clients.Index;
      import io.pinecone.configs.PineconeConfig;
      import io.pinecone.configs.PineconeConnection;
      import org.openapitools.db_data.client.ApiException;

      import java.util.*;

      public class UpsertText {
          public static void main(String[] args) throws ApiException {
              PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
              config.setHost("INDEX_HOST");
              PineconeConnection connection = new PineconeConnection(config);

              Index index = new Index(config, connection, "integrated-sparse-java");
              ArrayList<Map<String, String>> upsertRecords = new ArrayList<>();

              HashMap<String, String> record1 = new HashMap<>();
              record1.put("_id", "rec1");
              record1.put("category", "digestive system");
              record1.put("chunk_text", "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.");

              HashMap<String, String> record2 = new HashMap<>();
              record2.put("_id", "rec2");
              record2.put("category", "cultivation");
              record2.put("chunk_text", "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.");

              HashMap<String, String> record3 = new HashMap<>();
              record3.put("_id", "rec3");
              record3.put("category", "immune system");
              record3.put("chunk_text", "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.");

              HashMap<String, String> record4 = new HashMap<>();
              record4.put("_id", "rec4");
              record4.put("category", "endocrine system");
              record4.put("chunk_text", "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.");

              upsertRecords.add(record1);
              upsertRecords.add(record2);
              upsertRecords.add(record3);
              upsertRecords.add(record4);

              index.upsertRecords("example-namespace", upsertRecords);
          }
      }
      ```

      ```go Go
      package main

      import (
          "context"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
          if err != nil {
              log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      	  }

          // Upsert records into a namespace
          // `chunk_text` fields are converted to sparse vectors
          // `category` and `quarter` fields are stored as metadata
      	records := []*pinecone.IntegratedRecord{
      		{
      			"_id":        "vec1",
      			"chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
      			"category":   "technology",
      			"quarter":    "Q3",
      		},
      		{
      			"_id":        "vec2",
      			"chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
      			"category":   "technology",
      			"quarter":    "Q4",
      		},
      		{
      			"_id":        "vec3",
      			"chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
      			"category":   "technology",
      			"quarter":    "Q3",
      		},
      		{
      			"_id":        "vec4",
      			"chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
      			"category":   "technology",
      			"quarter":    "Q4",
      		},
      	}

      	err = idxConnection.UpsertRecords(ctx, records)
      	if err != nil {
      		log.Fatalf("Failed to upsert vectors: %v", err)
      	}
      }
      ```

      ```csharp C#
      using Pinecone;

      var pinecone = new PineconeClient("YOUR_API_KEY");

      var index = pinecone.Index(host: "INDEX_HOST");

      await index.UpsertRecordsAsync(
          "example-namespace",
          [
              new UpsertRecord
              {
                  Id = "rec1",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                      ["category"] = "technology",
                      ["quarter"] = "Q3",
                  },
              },
              new UpsertRecord
              {
                  Id = "rec2",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                      ["category"] = "technology",
                      ["quarter"] = "Q4",
                  },
              },  
              new UpsertRecord
              {
                  Id = "rec3",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                      ["category"] = "technology",
                      ["quarter"] = "Q4",
                  },
              },
              new UpsertRecord
              {
                  Id = "rec4",
                  AdditionalProperties =
                  {
                      ["chunk_text"] = "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                      ["category"] = "technology",
                      ["quarter"] = "Q3",
                  },
              },
          ]
      );
      ```

      ```shell curl
      INDEX_HOST="INDEX_HOST"
      NAMESPACE="YOUR_NAMESPACE"
      PINECONE_API_KEY="YOUR_API_KEY"

      curl  "https://$INDEX_HOST/records/namespaces/$NAMESPACE/upsert" \
          -H "Content-Type: application/x-ndjson" \
          -H "Api-Key: $PINECONE_API_KEY" \
          -H "X-Pinecone-API-Version: 2025-04" \
          -d '{ "_id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.", "category": "technology", "quarter": "Q3" }
            { "_id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.", "category": "technology", "quarter": "Q4" }
            { "_id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.", "category": "technology", "quarter": "Q3" }
            { "_id": "vec4", "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.", "category": "technology", "quarter": "Q4" }'
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Upsert vectors">
    To upsert sparse vectors into a [sparse index](/guides/index-data/create-an-index#create-a-sparse-index), use the [`upsert`](/reference/api/latest/data-plane/upsert) operation as follows:

    * Specify the [`namespace`](/guides/index-data/indexing-overview#namespaces) to upsert into. If the namespace doesn't exist, it is created. To use the default namespace, set the namespace to `"__default__"`.
    * Format your input data as records, each with the following:
      * An `id` field with a unique record identifier for the index namespace.
      * A `sparse_values` field with the sparse vector values and indices.
      * Optionally, a `metadata` field with [key-value pairs](/guides/index-data/indexing-overview#metadata) to store additional information or context. When you query the index, you can use metadata to [filter search results](/guides/search/filter-by-metadata).

    For example, the following code upserts sparse vector representations of sentences related to the term "apple", with the source text and additional fields stored as metadata:

    <CodeGroup>
      ```python Python
      from pinecone import Pinecone, SparseValues, Vector

      pc = Pinecone(api_key="YOUR_API_KEY")

      # To get the unique host for an index, 
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      index = pc.Index(host="INDEX_HOST")

      index.upsert(
          namespace="example-namespace",
          vectors=[
              {
                  "id": "vec1",
                  "sparse_values": {
                      "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688],
                      "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191]
                  },
                  "metadata": {
                      "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                      "category": "technology",
                      "quarter": "Q3"
                  }
              },
              {
                  "id": "vec2",
                  "sparse_values": {
                      "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469],
                      "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697]
                  },
                  "metadata": {
                      "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                      "category": "technology",
                      "quarter": "Q4"
                  }
              },
              {
                  "id": "vec3",
                  "sparse_values": {
                      "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094],
                      "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697]
                  },
                  "metadata": {
                      "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                      "category": "technology",
                      "quarter": "Q3"
                  }
              },
              {
                  "id": "vec4",
                  "sparse_values": {
                      "values": [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375],
                      "indices": [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673]
                  },
                  "metadata": {
                      "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                      "category": "technology",
                      "quarter": "Q4"
                  }
              }
          ]
      )
      ```

      ```javascript JavaScript
      import { Pinecone } from '@pinecone-database/pinecone'

      const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const index = pc.index("INDEX_NAME", "INDEX_HOST")

      await index.namespace('example-namespace').upsert([
        {
          id: 'vec1',
          sparseValues: {
            indices: [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191],
            values: [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688]
          },
          metadata: { 
            chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.', 
            category: 'technology',
            quarter: 'Q3' 
          }
        },
        {
          id: 'vec2',
          sparseValues: {
            indices: [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697],
            values: [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469]
          },
          metadata: { 
            chunk_text: "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.", 
            category: 'technology',
            quarter: 'Q4' 
          }
        },
        {
          id: 'vec3',
          sparseValues: {
            indices: [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697],
            values: [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094]
          },
          metadata: { 
            chunk_text: "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production", 
            category: 'technology',
            quarter: 'Q3' 
          }
        },
        {
          id: 'vec4',
          sparseValues: {
            indices: [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673],
            values: [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375]
          },
          metadata: { 
            chunk_text: 'AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.', 
            category: 'technology',
            quarter: 'Q4' 
          }
        }
      ]);
      ```

      ```java Java
      import io.pinecone.clients.Pinecone;
      import io.pinecone.clients.Index;
      import com.google.protobuf.Struct;
      import com.google.protobuf.Value;

      import java.util.*;

      public class UpsertSparseVectors {
          public static void main(String[] args) throws InterruptedException {
              // Instantiate Pinecone class
              Pinecone pinecone = new Pinecone.Builder("YOUR_API)KEY").build();
              
              Index index = pinecone.getIndexConnection("docs-example");

              // Record 1
              ArrayList<Long> indices1 = new ArrayList<>(Arrays.asList(
                      822745112L, 1009084850L, 1221765879L, 1408993854L, 1504846510L,
                      1596856843L, 1640781426L, 1656251611L, 1807131503L, 2543655733L,
                      2902766088L, 2909307736L, 3246437992L, 3517203014L, 3590924191L
              ));

              ArrayList<Float> values1 = new ArrayList<>(Arrays.asList(
                      1.7958984f, 0.41577148f, 2.828125f, 2.8027344f, 2.8691406f,
                      1.6533203f, 5.3671875f, 1.3046875f, 0.49780273f, 0.5722656f,
                      2.71875f, 3.0820312f, 2.5019531f, 4.4414062f, 3.3554688f
              ));

              Struct metaData1 = Struct.newBuilder()
                      .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.").build())
                      .putFields("category", Value.newBuilder().setStringValue("technology").build())
                      .putFields("quarter", Value.newBuilder().setStringValue("Q3").build())
                      .build();

              // Record 2
              ArrayList<Long> indices2 = new ArrayList<>(Arrays.asList(
                      131900689L, 592326839L, 710158994L, 838729363L, 1304885087L,
                      1640781426L, 1690623792L, 1807131503L, 2066971792L, 2428553208L,
                      2548600401L, 2577534050L, 3162218338L, 3319279674L, 3343062801L,
                      3476647774L, 3485013322L, 3517203014L, 4283091697L
              ));

              ArrayList<Float> values2 = new ArrayList<>(Arrays.asList(
                      0.4362793f, 3.3457031f, 2.7714844f, 3.0273438f, 3.3164062f,
                      5.6015625f, 2.4863281f, 0.38134766f, 1.25f, 2.9609375f,
                      0.34179688f, 1.4306641f, 0.34375f, 3.3613281f, 1.4404297f,
                      2.2558594f, 2.2597656f, 4.8710938f, 0.5605469f
              ));

              Struct metaData2 = Struct.newBuilder()
                      .putFields("chunk_text", Value.newBuilder().setStringValue("Analysts suggest that AAPL'\\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.").build())
                      .putFields("category", Value.newBuilder().setStringValue("technology").build())
                      .putFields("quarter", Value.newBuilder().setStringValue("Q4").build())
                      .build();

              // Record 3
              ArrayList<Long> indices3 = new ArrayList<>(Arrays.asList(
                      8661920L, 350356213L, 391213188L, 554637446L, 1024951234L,
                      1640781426L, 1780689102L, 1799010313L, 2194093370L, 2632344667L,
                      2641553256L, 2779594451L, 3517203014L, 3543799498L,
                      3837503950L, 4283091697L
              ));

              ArrayList<Float> values3 = new ArrayList<>(Arrays.asList(
                      2.6875f, 4.2929688f, 3.609375f, 3.0722656f, 2.1152344f,
                      5.78125f, 3.7460938f, 3.7363281f, 1.2695312f, 3.4824219f,
                      0.7207031f, 0.0826416f, 4.671875f, 3.7011719f, 2.796875f,
                      0.61621094f
              ));

              Struct metaData3 = Struct.newBuilder()
                      .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL'\\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production").build())
                      .putFields("category", Value.newBuilder().setStringValue("technology").build())
                      .putFields("quarter", Value.newBuilder().setStringValue("Q3").build())
                      .build();

              // Record 4
              ArrayList<Long> indices4 = new ArrayList<>(Arrays.asList(
                      131900689L, 152217691L, 441495248L, 1640781426L, 1851149807L,
                      2263326288L, 2502307765L, 2641553256L, 2684780967L, 2966813704L,
                      3162218338L, 3283104238L, 3488055477L, 3530642888L, 3888762515L,
                      4152503047L, 4177290673L
              ));

              ArrayList<Float> values4 = new ArrayList<>(Arrays.asList(
                      0.73046875f, 0.46972656f, 2.84375f, 5.2265625f, 3.3242188f,
                      1.9863281f, 0.9511719f, 0.5019531f, 4.4257812f, 3.4277344f,
                      0.41308594f, 4.3242188f, 2.4179688f, 3.1757812f, 1.0224609f,
                      2.0585938f, 2.5859375f
              ));

              Struct metaData4 = Struct.newBuilder()
                      .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space").build())
                      .putFields("category", Value.newBuilder().setStringValue("technology").build())
                      .putFields("quarter", Value.newBuilder().setStringValue("Q4").build())
                      .build();

              index.upsert("vec1", Collections.emptyList(), indices1, values1, metaData1, "example-namespace");
              index.upsert("vec2", Collections.emptyList(), indices2, values2, metaData2, "example-namespace");
              index.upsert("vec3", Collections.emptyList(), indices3, values3, metaData3, "example-namespace");
              index.upsert("vec4", Collections.emptyList(), indices4, values4, metaData4, "example-namespace");
      ```

      ```go Go
      package main

      import (
      	"context"
      	"fmt"
      	"log"

      	"github.com/pinecone-io/go-pinecone/v4/pinecone"
      	"google.golang.org/protobuf/types/known/structpb"
      )

      func main() {
      	ctx := context.Background()

      	pc, err := pinecone.NewClient(pinecone.NewClientParams{
      		ApiKey: "YOUR_API_KEY",
      	})
      	if err != nil {
      		log.Fatalf("Failed to create Client: %v", err)
      	}

      	// To get the unique host for an index,
      	// see https://docs.pinecone.io/guides/manage-data/target-an-index
      	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      	if err != nil {
      		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      	}

      	sparseValues1 := pinecone.SparseValues{
      		Indices: []uint32{822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191},
      		Values:  []float32{1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688},
      	}

      	metadataMap1 := map[string]interface{}{
      		"chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones",
      		"category":    "technology",
      		"quarter":     "Q3",
      	}

      	metadata1, err := structpb.NewStruct(metadataMap1)
      	if err != nil {
      		log.Fatalf("Failed to create metadata map: %v", err)
      	}

      	sparseValues2 := pinecone.SparseValues{
      		Indices: []uint32{131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697},
      		Values:  []float32{0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.560546},
      	}

      	metadataMap2 := map[string]interface{}{
      		"chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
      		"category":    "technology",
      		"quarter":     "Q4",
      	}

      	metadata2, err := structpb.NewStruct(metadataMap2)
      	if err != nil {
      		log.Fatalf("Failed to create metadata map: %v", err)
      	}

      	sparseValues3 := pinecone.SparseValues{
      		Indices: []uint32{8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697},
      		Values:  []float32{2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094},
      	}

      	metadataMap3 := map[string]interface{}{
      		"chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
      		"category":    "technology",
      		"quarter":     "Q3",
      	}

      	metadata3, err := structpb.NewStruct(metadataMap3)
      	if err != nil {
      		log.Fatalf("Failed to create metadata map: %v", err)
      	}

      	sparseValues4 := pinecone.SparseValues{
      		Indices: []uint32{131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673},
      		Values:  []float32{0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375},
      	}

      	metadataMap4 := map[string]interface{}{
      		"chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
      		"category":    "technology",
      		"quarter":     "Q4",
      	}

      	metadata4, err := structpb.NewStruct(metadataMap4)
      	if err != nil {
      		log.Fatalf("Failed to create metadata map: %v", err)
      	}

      	vectors := []*pinecone.Vector{
      		{
      			Id:           "vec1",
      			SparseValues: &sparseValues1,
      			Metadata:     metadata1,
      		},
      		{
      			Id:           "vec2",
      			SparseValues: &sparseValues2,
      			Metadata:     metadata2,
      		},
      		{
      			Id:           "vec3",
      			SparseValues: &sparseValues3,
      			Metadata:     metadata3,
      		},
      		{
      			Id:           "vec4",
      			SparseValues: &sparseValues4,
      			Metadata:     metadata4,
      		},
      	}

      	count, err := idxConnection.UpsertVectors(ctx, vectors)
      	if err != nil {
      		log.Fatalf("Failed to upsert vectors: %v", err)
      	} else {
      		fmt.Printf("Successfully upserted %d vector(s)!\n", count)
      	}
      }
      ```

      ```csharp C#
      using Pinecone;

      var pinecone = new PineconeClient("YOUR_API_KEY");

      var index = pinecone.Index("docs-example");

      var vector1 = new Vector
      {
          Id = "vec1",
          SparseValues = new SparseValues
          {
              Indices = new uint[] { 822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191 },
              Values = new ReadOnlyMemory<float>([1.7958984f, 0.41577148f, 2.828125f, 2.8027344f, 2.8691406f, 1.6533203f, 5.3671875f, 1.3046875f, 0.49780273f, 0.5722656f, 2.71875f, 3.0820312f, 2.5019531f, 4.4414062f, 3.3554688f])
          },
          Metadata = new Metadata {
              ["chunk_text"] = new("AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."),
              ["category"] = new("technology"),
              ["quarter"] = new("Q3"),
          },
      };

      var vector2 = new Vector
      {
          Id = "vec2",
          SparseValues = new SparseValues
          {
              Indices = new uint[] { 131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697 },
              Values = new ReadOnlyMemory<float>([0.4362793f, 3.3457031f, 2.7714844f, 3.0273438f, 3.3164062f, 5.6015625f, 2.4863281f, 0.38134766f, 1.25f, 2.9609375f, 0.34179688f, 1.4306641f, 0.34375f, 3.3613281f, 1.4404297f, 2.2558594f, 2.2597656f, 4.8710938f, 0.5605469f])
          },
          Metadata = new Metadata {
              ["chunk_text"] = new("Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."),
              ["category"] = new("technology"),
              ["quarter"] = new("Q4"),
          },
      };

      var vector3 = new Vector
      {
          Id = "vec3",
          SparseValues = new SparseValues
          {
              Indices = new uint[] { 8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697 },
              Values = new ReadOnlyMemory<float>([2.6875f, 4.2929688f, 3.609375f, 3.0722656f, 2.1152344f, 5.78125f, 3.7460938f, 3.7363281f, 1.2695312f, 3.4824219f, 0.7207031f, 0.0826416f, 4.671875f, 3.7011719f, 2.796875f, 0.61621094f])
          },
          Metadata = new Metadata {
              ["chunk_text"] = new("AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"),
              ["category"] = new("technology"),
              ["quarter"] = new("Q3"),
          },    
      };

      var vector4 = new Vector
      {
          Id = "vec4",
          SparseValues = new SparseValues
          {
              Indices = new uint[] { 131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673 },
              Values = new ReadOnlyMemory<float>([0.73046875f, 0.46972656f, 2.84375f, 5.2265625f, 3.3242188f, 1.9863281f, 0.9511719f, 0.5019531f, 4.4257812f, 3.4277344f, 0.41308594f, 4.3242188f, 2.4179688f, 3.1757812f, 1.0224609f, 2.0585938f, 2.5859375f])
          },
          Metadata = new Metadata {
              ["chunk_text"] = new("AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space."),
              ["category"] = new("technology"),
              ["quarter"] = new("Q4"),
          },
      };

      // Upsert vector
      Console.WriteLine("Upserting vector...");
      var upsertResponse = await index.UpsertAsync(new UpsertRequest
      {
          Vectors = new List<Vector> { vector1, vector2, vector3, vector4 },
          Namespace = "example-namespace"
      });
      Console.WriteLine($"Upserted {upsertResponse.UpsertedCount} vector");
      ```

      ```shell curl
      INDEX_HOST="INDEX_HOST"
      PINECONE_API_KEY="YOUR_API_KEY"

      curl "http://$INDEX_HOST/vectors/upsert" \
        -H "Content-Type: application/json" \
        -H "Api-Key: $PINECONE_API_KEY" \
        -H "X-Pinecone-API-Version: 2025-04" \
        -d '{
              "namespace": "example-namespace",
              "vectors": [
                  {
                      "id": "vec1",
                      "sparseValues": {
                          "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688],
                          "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191]
                      },
                      "metadata": {
                          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                          "category": "technology",
                          "quarter": "Q3"
                      }
                  },
                  {
                      "id": "vec2",
                      "sparseValues": {
                          "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469],
                          "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697]
                      },
                      "metadata": {
                          "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                          "category": "technology",
                          "quarter": "Q4"
                      }
                  },
                  {
                      "id": "vec3",
                      "sparseValues": {
                          "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094],
                          "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697]
                      },
                      "metadata": {
                          "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                          "category": "technology",
                          "quarter": "Q3"
                      }
                  },
                  {
                      "id": "vec4",
                      "sparseValues": {
                          "values": [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375],
                          "indices": [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673]
                      },
                      "metadata": {
                          "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                          "category": "technology",
                          "quarter": "Q4"
                      }
                  },
              ]
          }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Upsert in batches

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

Send upserts in batches to help increase throughput.

* When upserting records with vectors, a batch should be as large as possible (up to 1000 records) without exceeding the [max request size of 2 MB](#upsert-limits).

  To understand the number of records you can fit into one batch based on the vector dimensions and metadata size, see the following table:

  | Dimension | Metadata (bytes) | Max batch size |
  | :-------- | :--------------- | :------------- |
  | 386       | 0                | 1000           |
  | 768       | 500              | 559            |
  | 1536      | 2000             | 245            |

* When upserting records with text, a batch can contain up to 96 records. This limit comes from the [hosted embedding models](/guides/index-data/create-an-index#embedding-models) used during integrated embedding rather than the batch size limit for upserting raw vectors.

<CodeGroup>
  ```Python Python
  import random
  import itertools
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  def chunks(iterable, batch_size=200):
      """A helper function to break an iterable into chunks of size batch_size."""
      it = iter(iterable)
      chunk = tuple(itertools.islice(it, batch_size))
      while chunk:
          yield chunk
          chunk = tuple(itertools.islice(it, batch_size))

  vector_dim = 128
  vector_count = 10000

  # Example generator that generates many (id, vector) pairs
  example_data_generator = map(lambda i: (f'id-{i}', [random.random() for _ in range(vector_dim)]), range(vector_count))

  # Upsert data with 200 vectors per upsert request
  for ids_vectors_chunk in chunks(example_data_generator, batch_size=200):
      index.upsert(vectors=ids_vectors_chunk) 
  ```

  ```JavaScript JavaScript
  import { Pinecone } from "@pinecone-database/pinecone";

  const RECORD_COUNT = 10000;
  const RECORD_DIMENSION = 128;

  const client = new Pinecone({ apiKey: "YOUR_API_KEY" });
  const index = client.index("docs-example");

  // A helper function that breaks an array into chunks of size batchSize
  const chunks = (array, batchSize = 200) => {
    const chunks = [];

    for (let i = 0; i < array.length; i += batchSize) {
      chunks.push(array.slice(i, i + batchSize));
    }

    return chunks;
  };

  // Example data generation function, creates many (id, vector) pairs
  const generateExampleData = () =>
    Array.from({ length: RECORD_COUNT }, (_, i) => {
      return {
        id: `id-${i}`,
        values: Array.from({ length: RECORD_DIMENSION }, (_, i) => Math.random()),
      };
    });

  const exampleRecordData = generateExampleData();
  const recordChunks = chunks(exampleRecordData);

  // Upsert data with 200 records per upsert request
  for (const chunk of recordChunks) {
    await index.upsert(chunk)
  }
  ```

  ```java Java
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.unsigned_indices_model.VectorWithUnsignedIndices;

  import java.util.Arrays;
  import java.util.List;

  public class UpsertBatchExample  {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");

          ArrayList<VectorWithUnsignedIndices> vectors = generateVectors();
          ArrayList<ArrayList<VectorWithUnsignedIndices>> chunks = chunks(vectors, BATCH_SIZE);

          for (ArrayList<VectorWithUnsignedIndices> chunk : chunks) {
              index.upsert(chunk, "example-namespace");
          }
      }

      // A helper function that breaks an ArrayList into chunks of batchSize
      private static ArrayList<ArrayList<VectorWithUnsignedIndices>> chunks(ArrayList<VectorWithUnsignedIndices> vectors, int batchSize) {
          ArrayList<ArrayList<VectorWithUnsignedIndices>> chunks = new ArrayList<>();
          ArrayList<VectorWithUnsignedIndices> chunk = new ArrayList<>();

          for (int i = 0; i < vectors.size(); i++) {
              if (i % BATCH_SIZE == 0 && i != 0) {
                  chunks.add(chunk);
                  chunk = new ArrayList<>();
              }

              chunk.add(vectors.get(i));
          }

          return chunks;
      }

      // Example data generation function, creates many (id, vector) pairs
      private static ArrayList<VectorWithUnsignedIndices> generateVectors() {
          Random random = new Random();
          ArrayList<VectorWithUnsignedIndices> vectors = new ArrayList<>();


          for (int i = 0; i <= RECORD_COUNT; i++) {
              String id = "id-" + i;
              ArrayList<Float> values = new ArrayList<>();

              for (int j = 0; j < RECORD_DIMENSION; j++) {
                  values.add(random.nextFloat());
              }

              VectorWithUnsignedIndices vector = new VectorWithUnsignedIndices();
              vector.setId(id);
              vector.setValues(values);
              vectors.add(vector);
          }

          return vectors;
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	  }

      // Generate a large number of vectors to upsert
      vectorCount := 10000
      vectorDim := idx.Dimension

      vectors := make([]*pinecone.Vector, vectorCount)
      for i := 0; i < int(vectorCount); i++ {
          randomFloats := make([]float32, vectorDim)

          for i := int32(0); i < vectorDim; i++ {
              randomFloats[i] = rand.Float32()
          }

          vectors[i] = &pinecone.Vector{
              Id:     fmt.Sprintf("doc1#-vector%d", i),
              Values: randomFloats,
          }
      }

      // Break the vectors into batches of 200
      var batches [][]*pinecone.Vector
      batchSize := 200

      for len(vectors) > 0 {
          batchEnd := batchSize
          if len(vectors) < batchSize {
              batchEnd = len(vectors)
          }
          batches = append(batches, vectors[:batchEnd])
          vectors = vectors[batchEnd:]
      }

      // Upsert batches
      for i, batch := range batches {
          upsertResp, err := idxConn.UpsertVectors(context.Background(), batch)
          if err != nil {
              panic(err)
          }

          fmt.Printf("upserted %d vectors (%v of %v batches)\n", upsertResp, i+1, len(batches))
      }
  }
  ```
</CodeGroup>

## Upsert in parallel

<Tip>
  Python SDK v6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Asyncio support makes it possible to use Pinecone with modern async web frameworks such as FastAPI, Quart, and Sanic. For more details, see [Asyncio support](/reference/python-sdk#asyncio-support).
</Tip>

Send multiple upserts in parallel to help increase throughput. Vector operations block until the response has been received. However, they can be made asynchronously as follows:

<CodeGroup>
  ```Python Python
  # This example uses `async_req=True` and multiple threads.
  # For a single-threaded approach compatible with modern async web frameworks, 
  # see https://docs.pinecone.io/reference/python-sdk#asyncio-support
  import random
  import itertools
  from pinecone import Pinecone

  # Initialize the client with pool_threads=30. This limits simultaneous requests to 30.
  pc = Pinecone(api_key="YOUR_API_KEY", pool_threads=30)

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  def chunks(iterable, batch_size=200):
      """A helper function to break an iterable into chunks of size batch_size."""
      it = iter(iterable)
      chunk = tuple(itertools.islice(it, batch_size))
      while chunk:
          yield chunk
          chunk = tuple(itertools.islice(it, batch_size))

  vector_dim = 128
  vector_count = 10000

  example_data_generator = map(lambda i: (f'id-{i}', [random.random() for _ in range(vector_dim)]), range(vector_count))

  # Upsert data with 200 vectors per upsert request asynchronously
  # - Pass async_req=True to index.upsert()
  with pc.Index(host="INDEX_HOST", pool_threads=30) as index:
      # Send requests in parallel
      async_results = [
          index.upsert(vectors=ids_vectors_chunk, async_req=True)
          for ids_vectors_chunk in chunks(example_data_generator, batch_size=200)
      ]
      # Wait for and retrieve responses (this raises in case of error)
      [async_result.get() for async_result in async_results]
  ```

  ```JavaScript JavaScript
  import { Pinecone } from "@pinecone-database/pinecone";

  const RECORD_COUNT = 10000;
  const RECORD_DIMENSION = 128;

  const client = new Pinecone({ apiKey: "YOUR_API_KEY" });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  // A helper function that breaks an array into chunks of size batchSize
  const chunks = (array, batchSize = 200) => {
    const chunks = [];

    for (let i = 0; i < array.length; i += batchSize) {
      chunks.push(array.slice(i, i + batchSize));
    }

    return chunks;
  };

  // Example data generation function, creates many (id, vector) pairs
  const generateExampleData = () =>
    Array.from({ length: RECORD_COUNT }, (_, i) => {
      return {
        id: `id-${i}`,
        values: Array.from({ length: RECORD_DIMENSION }, (_, i) => Math.random()),
      };
    });

  const exampleRecordData = generateExampleData();
  const recordChunks = chunks(exampleRecordData);

  // Upsert data with 200 records per request asynchronously using Promise.all()
  await Promise.all(recordChunks.map((chunk) => index.upsert(chunk)));
  ```

  ```java Java
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.UpsertResponse;
  import io.pinecone.unsigned_indices_model.VectorWithUnsignedIndices;

  import java.util.ArrayList;
  import java.util.Arrays;
  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;
  import java.util.List;

  public class UpsertExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");

          // Run 5 threads concurrently and upsert data into pinecone
          int numberOfThreads = 5;

          // Create a fixed thread pool
          ExecutorService executor = Executors.newFixedThreadPool(numberOfThreads);

          // Submit tasks to the executor
          for (int i = 0; i < numberOfThreads; i++) {
              // upsertData
              int batchNumber = i+1;
              executor.submit(() -> upsertData(index, batchNumber));
          }

          // Shutdown the executor
          executor.shutdown();
      }

      private static void upsertData(Index index, int batchNumber) {
          // Vector ids to be upserted
          String prefix = "v" + batchNumber;
          List<String> upsertIds = Arrays.asList(prefix + "_1", prefix + "_2", prefix + "_3");

          // List of values to be upserted
          List<List<Float>> values = new ArrayList<>();
          values.add(Arrays.asList(1.0f, 2.0f, 3.0f));
          values.add(Arrays.asList(4.0f, 5.0f, 6.0f));
          values.add(Arrays.asList(7.0f, 8.0f, 9.0f));

          // List of sparse indices to be upserted
          List<List<Long>> sparseIndices = new ArrayList<>();
          sparseIndices.add(Arrays.asList(1L, 2L, 3L));
          sparseIndices.add(Arrays.asList(4L, 5L, 6L));
          sparseIndices.add(Arrays.asList(7L, 8L, 9L));

          // List of sparse values to be upserted
          List<List<Float>> sparseValues = new ArrayList<>();
          sparseValues.add(Arrays.asList(1000f, 2000f, 3000f));
          sparseValues.add(Arrays.asList(4000f, 5000f, 6000f));
          sparseValues.add(Arrays.asList(7000f, 8000f, 9000f));

          List<VectorWithUnsignedIndices> vectors = new ArrayList<>(3);

          // Metadata to be upserted
          Struct metadataStruct1 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("action").build())
                  .putFields("year", Value.newBuilder().setNumberValue(2019).build())
                  .build();

          Struct metadataStruct2 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("thriller").build())
                  .putFields("year", Value.newBuilder().setNumberValue(2020).build())
                  .build();

          Struct metadataStruct3 = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder().setStringValue("comedy").build())
                  .putFields("year", Value.newBuilder().setNumberValue(2021).build())
                  .build();
          List<Struct> metadataStructList = Arrays.asList(metadataStruct1, metadataStruct2, metadataStruct3);

          // Upsert data
          for (int i = 0; i < metadataStructList.size(); i++) {
              vectors.add(buildUpsertVectorWithUnsignedIndices(upsertIds.get(i), values.get(i), sparseIndices.get(i), sparseValues.get(i), metadataStructList.get(i)));
          }

          UpsertResponse upsertResponse = index.upsert(vectors, "example-namespace");
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"
      "math/rand"
      "sync"
      
      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConn, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	  }

      // Generate a large number of vectors to upsert
      vectorCount := 10000
      vectorDim := idx.Dimension

      vectors := make([]*pinecone.Vector, vectorCount)
      for i := 0; i < int(vectorCount); i++ {
          randomFloats := make([]float32, vectorDim)

          for i := int32(0); i < vectorDim; i++ {
              randomFloats[i] = rand.Float32()
          }

          vectors[i] = &pinecone.Vector{
              Id:     fmt.Sprintf("doc1#-vector%d", i),
              Values: randomFloats,
          }
      }

      // Break the vectors into batches of 200
      var batches [][]*pinecone.Vector
      batchSize := 200

      for len(vectors) > 0 {
          batchEnd := batchSize
          if len(vectors) < batchSize {
              batchEnd = len(vectors)
          }
          batches = append(batches, vectors[:batchEnd])
          vectors = vectors[batchEnd:]
      }

      // Use channels to manage concurrency and possible errors
      maxConcurrency := 10
      errChan := make(chan error, len(batches))
      semaphore := make(chan struct{}, maxConcurrency)
      var wg sync.WaitGroup

      for i, batch := range batches {
          wg.Add(1)
          semaphore <- struct{}{}

          go func(batch []*pinecone.Vector, i int) {
              defer wg.Done()
              defer func() { <-semaphore }()

              upsertResp, err := idxConn.UpsertVectors(context.Background(), batch)
              if err != nil {
                  errChan <- fmt.Errorf("batch %d failed: %v", i, err)
                  return
              }

              fmt.Printf("upserted %d vectors (%v of %v batches)\n", upsertResp, i+1, len(batches))
          }(batch, i)
      }

      wg.Wait()
      close(errChan)

      for err := range errChan {
          if err != nil {
              fmt.Printf("Error while upserting batch: %v\n", err)
          }
      }
  }
  ```
</CodeGroup>

### Python SDK with gRPC

Using the Python SDK with gRPC extras can provide higher upsert speeds. Through multiplexing, gRPC is able to handle large amounts of requests in parallel without slowing down the rest of the system (HoL blocking), unlike REST. Moreover, you can pass various retry strategies to the gRPC SDK, including exponential backoffs.

To install the gRPC version of the SDK:

```Shell Shell
pip install "pinecone[grpc]"
```

To use the gRPC SDK, import the `pinecone.grpc` subpackage and target an index as usual:

```Python Python
from pinecone.grpc import PineconeGRPC as Pinecone

# This is gRPC client aliased as "Pinecone"
pc = Pinecone(api_key='YOUR_API_KEY')  

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")
```

To launch multiple read and write requests in parallel, pass `async_req` to the `upsert` operation:

```Python Python
def chunker(seq, batch_size):
  return (seq[pos:pos + batch_size] for pos in range(0, len(seq), batch_size))

async_results = [
  index.upsert(vectors=chunk, async_req=True)
  for chunk in chunker(data, batch_size=200)
]

# Wait for and retrieve responses (in case of error)
[async_result.result() for async_result in async_results]
```

<Note>
  It is possible to get write-throttled faster when upserting using the gRPC SDK. If you see this often, we recommend you use a backoff algorithm(e.g., [exponential backoffs](https://www.pinecone.io/blog/working-at-scale/))\
  while upserting.

  The syntax for upsert, query, fetch, and delete with the gRPC SDK remain the same as the standard SDK.
</Note>

## Upsert limits

| Metric                                                             | Limit                                                         |
| :----------------------------------------------------------------- | :------------------------------------------------------------ |
| Max [batch size](/guides/index-data/upsert-data#upsert-in-batches) | 2 MB or 1000 records with vectors <br /> 96 records with text |
| Max metadata size per record                                       | 40 KB                                                         |
| Max length for a record ID                                         | 512 characters                                                |
| Max dimensionality for dense vectors                               | 20,000                                                        |
| Max non-zero values for sparse vectors                             | 2048                                                          |
| Max dimensionality for sparse vectors                              | 4.2 billion                                                   |

# Import records

This page shows you how to import records from Amazon S3, Google Cloud Storage, or Azure Blob Storage into an index. Importing from object storage is the most efficient and cost-effective way to load large numbers of records into an index.

To run through this guide in your browser, see the [Bulk import colab notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-import.ipynb).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

## Before you import

Before you can import records, ensure you have a serverless index, a storage integration, and data formatted in a Parquet file and uploaded to an Amazon S3 bucket, Google Cloud Storage bucket, or Azure Blob Storage container.

### Create an index

[Create a serverless index](/guides/index-data/create-an-index) for your data.

Be sure to create your index on a cloud that supports importing from the object storage you want to use:

| Index location | AWS S3 | Google Cloud Storage | Azure Blob Storage |
| -------------- | :----: | :------------------: | :----------------: |
| **AWS**        |    ✅   |           ✅          |          ✅         |
| **GCP**        |    ❌   |           ✅          |          ✅         |
| **Azure**      |    ❌   |           ✅          |          ✅         |

### Add a storage integration

To import records from a public data source, a storage integration is not required. However, to import records from a secure data source, you must create an integration to allow Pinecone access to data in your object storage. See the following guides:

* [Integrate with Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3)
* [Integrate with Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage)
* [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)

### Prepare your data

1. In your Amazon S3 bucket, Google Cloud Storage bucket, or Azure Blob Storage container, create an import directory containing a subdirectory for each namespace you want to import into. The namespaces must not yet exist in your index.

   For example, to import data into the namespaces `example_namespace1` and `example_namespace2`, your directory structure would look like this:

   ```
   <BUCKET_OR_CONTAINER_NAME>/
   --/<IMPORT_DIR>/
   ----/example_namespace1/
   ----/example_namespace2/
   ```

   <Tip>
     To import into the default namespace, use a subdirectory called `__default__`. The default namespace must be empty.
   </Tip>

2. For each namespace, create one or more Parquet files defining the records to import.

   Parquet files must contain specific columns, depending on the index type:

   <Tabs>
     <Tab title="Dense index">
       To import into a namespace in a [dense index](/guides/index-data/indexing-overview#dense-indexes), the Parquet file must contain the following columns:

       | Column name | Parquet type  | Description                                                                                                                     |
       | ----------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
       | `id`        | `STRING`      | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                      |
       | `values`    | `LIST<FLOAT>` | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/concepts#dense-vector). |
       | `metadata`  | `STRING`      | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`. |

       <Warning>
         The Parquet file cannot contain additional columns.
       </Warning>

       For example:

       ```parquet
       id | values                   | metadata
       --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       1  | [ 3.82  2.48 -4.15 ... ] | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
       2  | [ 1.82  3.48 -2.15 ... ] | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
       ```
     </Tab>

     <Tab title="Sparse index">
       To import into a namespace in a [sparse index](/guides/index-data/indexing-overview#sparse-indexes), the Parquet file must contain the following columns:

       | Column name     | Parquet type                  | Description                                                                                                                                                                                     |
       | --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | `id`            | `STRING`                      | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                                                                                      |
       | `sparse_values` | `LIST<INT>` and `LIST<FLOAT>` | Required. A list of floating-point values (sparse values) and a list of integer values (sparse indices) that make up the [sparse vector embedding](/guides/get-started/concepts#sparse-vector). |
       | `metadata`      | `STRING`                      | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`.                                                                 |

       <Warning>
         The Parquet file cannot contain additional columns.
       </Warning>

       For example:

       ```parquet
       id | sparse_values                                                                                       | metadata
       --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       1  | {"indices": [ 822745112 1009084850 1221765879 ... ], "values": [1.7958984 0.41577148 2.828125 ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
       2  | {"indices": [ 504939989 1293001993 3201939490 ... ], "values": [1.4383747 0.72849722 1.384775 ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
       ```
     </Tab>

     <Tab title="Hybrid index">
       To import into a namespace in a [hybrid index](/guides/search/hybrid-search#use-a-single-hybrid-index), the Parquet file must contain the following columns:

       | Column name     | Parquet type                                          | Description                                                                                                                                                               |
       | --------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | `id`            | `STRING`                                              | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                                                                |
       | `values`        | `LIST<FLOAT>`                                         | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/concepts#dense-vector).                                           |
       | `sparse_values` | `STRUCT<indices: LIST<UINT_32>, values: LIST<FLOAT>>` | Optional. A list of floating-point values that make up the [sparse vector embedding](/guides/get-started/concepts#sparse-vector). To omit from specific rows, use `NULL`. |
       | `metadata`      | `STRING`                                              | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`.                                           |

       <Warning>
         The Parquet file cannot contain additional columns.
       </Warning>

       For example:

       ```parquet
       id | values                   | sparse_values                                                                          | metadata
       --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       1  | [ 3.82  2.48 -4.15 ... ] | {"indices": [1082468256, 1009084850, 1221765879, ...], "values": [2.0, 3.0, 4.0, ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
       2  | [ 1.82  3.48 -2.15 ... ] | {"indices": [2225824123, 1293001993, 3201939490, ...], "values": [5.0, 2.0, 3.0, ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
       ```
     </Tab>
   </Tabs>

3. Upload the Parquet files into the relevant subdirectory.

   For example, if you have subdirectories for the namespaces `example_namespace1` and `example_namespace2` and upload 4 Parquet files into each, your directory structure would look as follows after the upload:

   ```
   <BUCKET_OR_CONTAINER_NAME>/
   --/<IMPORT_DIR>/
   ----/example_namespace1/
   ------0.parquet
   ------1.parquet
   ------2.parquet
   ------3.parquet
   ----/example_namespace2/
   ------4.parquet
   ------5.parquet
   ------6.parquet
   ------7.parquet
   ```

## Import records into an index

<Warning>
  Review current [limitations](#limitations) before starting an import.
</Warning>

Use the [`start_import`](/reference/api/latest/data-plane/start_import) operation to start an asynchronous import of vectors from object storage into an index.

* For `uri`, specify the URI of the bucket and import directory containing the namespaces and Parquet files you want to import. For example:

  * Amazon S3: `s3://BUCKET_NAME/IMPORT_DIR`
  * Google Cloud Storage: `gs://BUCKET_NAME/IMPORT_DIR`
  * Azure Blob Storage: `https://STORAGE_ACCOUNT.blob.core.windows.net/CONTAINER_NAME/IMPORT_DIR`

* For `integration_id`, specify the Integration ID of the Amazon S3, Google Cloud Storage, or Azure Blob Storage integration you created. The ID is found on the [Storage integrations](https://app.pinecone.io/organizations/-/projects/-/storage) page of the Pinecone console.

  <Note>
    An Integration ID is not needed to import from a public bucket.
  </Note>

* For `error_mode`, use `CONTINUE` or `ABORT`.

  * With `ABORT`, the operation stops if any records fail to import.
  * With `CONTINUE`, the operation continues on error, but there is not any notification about which records, if any, failed to import. To see how many records were successfully imported, use the [`describe_import`](#describe-an-import) operation.

<CodeGroup>
  ```python Python
  from pinecone import Pinecone, ImportErrorMode

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")
  root = "s3://example_bucket/import"

  index.start_import(
      uri=root,
      integration_id="a12b3d4c-47d2-492c-a97a-dd98c8dbefde", # Optional for public buckets
      error_mode=ImportErrorMode.CONTINUE # or ImportErrorMode.ABORT
  )
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const storageURI = 's3://example_bucket/import';
  const errorMode = 'continue'; // or 'abort'
  const integrationID = 'a12b3d4c-47d2-492c-a97a-dd98c8dbefde'; // Optional for public buckets

  await index.startImport(storageURI, errorMode, integrationID); 
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.ImportErrorMode;
  import org.openapitools.db_data.client.model.StartImportResponse;

  public class StartImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // s3 uri
          String uri = "s3://example_bucket/import";

          // Integration ID (optional for public buckets)
          String integrationId = "a12b3d4c-47d2-492c-a97a-dd98c8dbefde";

          // Start an import
          StartImportResponse response = asyncIndex.startImport(uri, integrationId, ImportErrorMode.OnErrorEnum.CONTINUE);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

      uri := "s3://example_bucket/import"
      errorMode := "continue" // or "abort"
      importRes, err := idxConnection.StartImport(ctx, uri, nil, (*pinecone.ImportErrorMode)(&errorMode))
      if err != nil {
          log.Fatalf("Failed to start import: %v", err)
      }
      fmt.Printf("Import started with ID: %s", importRes.Id)
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var uri = "s3://example_bucket/import";

  var response = await index.StartBulkImportAsync(new StartImportRequest
  {
      Uri = uri,
      IntegrationId = "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
      ErrorMode = new ImportErrorMode { OnError = ImportErrorModeOnError.Continue }
  });
  ```

  ```bash curl
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/bulk/imports" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -H 'X-Pinecone-API-Version: 2025-04' \
    -d '{
          "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
          "uri": "s3://example_bucket/import",
          "errorMode": {
              "onError": "continue"
              }
          }'
  ```
</CodeGroup>

The response contains an `id` that you can use to [check the status of the import](#list-imports):

```json Response
{
   "id": "101"
}
```

Once all the data is loaded, the [index builder](/guides/get-started/database-architecture#index-builder) indexes the records, which usually takes at least 10 minutes. During this indexing process, the expected job status is `InProgress`, but `100.0` percent complete. Once all the imported records are indexed and fully available for querying, the import operation is set to `Completed`.

<Tip>
  You can start a new import using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). Find the index you want to import into, and click the **ellipsis (..) menu > Import data**.
</Tip>

## Track import progress

The amount of time required for an import depends on various factors, including:

* The number of records to import
* The number of namespaces to import, and the the number of records in each
* The total size (in bytes) of the import

To track an import's progress, check its status bar in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import) or use the [`describe_import`](/reference/api/latest/data-plane/describe_import) operation with the import ID:

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.describe_import(id="101")
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });


  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const results = await index.describeImport(id='101');
  console.log(results);
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.ImportModel;

  public class DescribeImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // Describe import
          ImportModel importDetails = asyncIndex.describeImport("101");

          System.out.println(importDetails);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      importID := "101"

      importDesc, err := idxConnection.DescribeImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to describe import: %s - %v", importID, err)
      }
      fmt.Printf("Import ID: %s, Status: %s", importDesc.Id, importDesc.Status)
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var importDetails = await index.DescribeBulkImportAsync("101");
  ```

  ```bash curl
  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://{INDEX_HOST}/bulk/imports/101" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H 'X-Pinecone-API-Version: 2025-04'
  ```
</CodeGroup>

The response contains the import details, including the import `status`, `percent_complete`, and `records_imported`:

```json Response
{
  "id": "101",
  "uri": "s3://example_bucket/import",
  "status": "InProgress",
  "created_at": "2024-08-19T20:49:00.754Z",
  "finished_at": "2024-08-19T20:49:00.754Z",
  "percent_complete": 42.2,
  "records_imported": 1000000
}
```

If the import fails, the response contains an `error` field with the reason for the failure:

```json Response
{
  "id": "102",
  "uri": "s3://example_bucket/import",
  "status": "Failed",
  "percent_complete": 0.0,
  "records_imported": 0,
  "created_at": "2025-08-21T11:29:47.886797+00:00",
  "error": "User error: The namespace \"namespace1\" already exists. Imports are only allowed into nonexistent namespaces.",
  "finished_at": "2025-08-21T11:30:05.506423+00:00"
}
```

## Manage imports

### List imports

Use the [`list_imports`](/reference/api/latest/data-plane/list_imports) operation to list all of the recent and ongoing imports. By default, the operation returns up to 100 imports per page. If the `limit` parameter is passed, the operation returns up to that number of imports per page instead. For example, if `limit=3`, up to 3 imports are returned per page. Whenever there are additional imports to return, the response includes a `pagination_token` for fetching the next page of imports.

<Tabs>
  <Tab title="Python SDK">
    When using the Python SDK, `list_import` paginates automatically.

    ```python Python
    from pinecone import Pinecone, ImportErrorMode

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    # List using a generator that handles pagination
    for i in index.list_imports():
        print(f"id: {i.id} status: {i.status}")

    # List using a generator that fetches all results at once
    operations = list(index.list_imports())
    print(operations)
    ```

    ```json Response
    {
      "data": [
        {
          "id": "1",
          "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
          "status": "Pending",
          "started_at": "2024-08-19T20:49:00.754Z",
          "finished_at": "2024-08-19T20:49:00.754Z",
          "percent_complete": 42.2,
          "records_imported": 1000000
        }
      ],
      "pagination": {
        "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
      }
    }
    ```

    <Tip>
      You can view the list of imports for an index in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/). Select the index and navigate to the **Imports** tab.
    </Tip>
  </Tab>

  <Tab title="Other SDKs">
    When using the Node.js SDK, Java SDK, Go SDK, .NET SDK, or REST API to list recent and ongoing imports, you must manually fetch each page of results. To view the next page of results, include the `paginationToken` provided in the response.

    <CodeGroup>
      ```javascript JavaScript
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const index = pc.index("INDEX_NAME", "INDEX_HOST")

      const results = await index.listImports({ limit: 10, paginationToken: 'Tm90aGluZyB0byBzZWUgaGVyZQo' });
      console.log(results);
      ```

      ```java Java
      import io.pinecone.clients.Pinecone;
      import io.pinecone.clients.AsyncIndex;
      import org.openapitools.db_data.client.ApiException;
      import org.openapitools.db_data.client.model.ListImportsResponse;

      public class ListImports {
          public static void main(String[] args) throws ApiException {
              // Initialize a Pinecone client with your API key
              Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

              // Get async imports connection object
              AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

              // List imports
              ListImportsResponse response = asyncIndex.listImports(10, "Tm90aGluZyB0byBzZWUgaGVyZQo");

              System.out.println(response);
          }
      }
      ```

      ```go Go
      package main

      import (
          "context"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
          if err != nil {
              log.Fatalf("Failed to create IndexConnection for Host: %v", err)
        	}

          limit := int32(10)
          firstImportPage, err := idxConnection.ListImports(ctx, &limit, nil)
          if err != nil {
              log.Fatalf("Failed to list imports: %v", err)
          }
          fmt.Printf("First page of imports: %+v", firstImportPage.Imports)

          paginationToken := firstImportPage.NextPaginationToken
          nextImportPage, err := idxConnection.ListImports(ctx, &limit, paginationToken)
          if err != nil {
              log.Fatalf("Failed to list imports: %v", err)
          }
          fmt.Printf("Second page of imports: %+v", nextImportPage.Imports)
      }
      ```

      ```csharp C#
      using Pinecone;

      var pinecone = new PineconeClient("YOUR_API_KEY");

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      var index = pinecone.Index(host: "INDEX_HOST");

      var imports = await index.ListBulkImportsAsync(new ListBulkImportsRequest
      {
          Limit = 10,
          PaginationToken = "Tm90aGluZyB0byBzZWUgaGVyZQo"
      });
      ```

      ```bash curl
      # To get the unique host for an index,
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      PINECONE_API_KEY="YOUR_API_KEY"
      INDEX_HOST="INDEX_HOST"

      curl -X GET "https://$INDEX_HOST/bulk/imports?paginationToken==Tm90aGluZyB0byBzZWUgaGVyZQo" \
        -H 'Api-Key: $YOUR_API_KEY' \
        -H 'X-Pinecone-API-Version: 2025-04'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Cancel an import

The [`cancel_import`](/reference/api/latest/data-plane/cancel_import) operation cancels an import if it is not yet finished. It has no effect if the import is already complete.

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.cancel_import(id="101")
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.cancelImport(id='101');
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;

  public class CancelImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // Cancel import
          asyncIndex.cancelImport("2");
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      importID := "101"

      err = idxConnection.CancelImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to cancel import: %s", importID)
      }

      importDesc, err := idxConnection.DescribeImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to describe import: %s - %v", importID, err)
      }
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var cancelResponse = await index.CancelBulkImportAsync("101");
  ```

  ```bash curl
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X DELETE "https://{INDEX_HOST}/bulk/imports/101" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

```json Response
{}
```

<Tip>
  You can cancel your import using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import). To cancel an ongoing import, select the index you are importing into and navigate to the **Imports** tab. Then, click the **ellipsis (..) menu > Cancel**.
</Tip>

## Import limits

| Metric                            | Limit                       |
| :-------------------------------- | :-------------------------- |
| Max size per import request       | 2 TB or 200,000,000 records |
| Max namespaces per import request | 10,000                      |
| Max files per import request      | 100,000                     |
| Max size per file                 | 10 GB                       |

Also:

* You cannot import data from an AWS S3 bucket into a Pinecone index hosted on GCP or Azure.
* You cannot import data from S3 Express One Zone storage.
* You cannot import data into an existing namespace.
* When importing data into the `__default__` namespace of an index, the default namespace must be empty.
* Each import takes at least 10 minutes to complete.
* When importing into an [index with integrated embedding](/guides/index-data/indexing-overview#vector-embedding), records must contain vectors, not text. To add records with text, you must use [upsert](/guides/index-data/upsert-data).

## See also

* [Integrate with Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3)
* [Integrate with Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage)
* [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)
* [Pinecone's pricing](https://www.pinecone.io/pricing/)

# Search overview

This section of the documentation shows you the different ways to search your data in Pinecone.

## Search types

* [Semantic search](/guides/search/semantic-search)
* [Lexical search](/guides/search/lexical-search)
* [Hybrid search](/guides/search/hybrid-search)

## Optimization

* [Filter by metadata](/guides/search/filter-by-metadata)
* [Rerank results](/guides/search/rerank-results)
* [Parallel queries](/guides/search/semantic-search#parallel-queries)

## Limits

| Metric            | Limit  |
| :---------------- | :----- |
| Max `top_k` value | 10,000 |
| Max result size   | 4MB    |

The query result size is affected by the dimension of the dense vectors and whether or not dense vector values and metadata are included in the result.

<Tip>
  If a query fails due to exceeding the 4MB result size limit, choose a lower `top_k` value, or use `include_metadata=False` or `include_values=False` to exclude metadata or values from the result.
</Tip>

## Cost

* To understand how cost is calculated for queries, see [Understanding cost](/guides/manage-cost/understanding-cost#query).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).

# Semantic search

This page shows you how to search a [dense index](/guides/index-data/indexing-overview#dense-indexes) for records that are most similar in meaning and context to a query. This is often called semantic search, nearest neighbor search, similarity search, or just vector search.

Semantic search uses [dense vectors](https://www.pinecone.io/learn/vector-embeddings/). Each number in a dense vector corresponds to a point in a multidimensional space. Vectors that are closer together in that space are semantically similar.

## Search with text

<Note>
  Searching with text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
</Note>

To search a dense index with a query text, use the [`search_records`](/reference/api/latest/data-plane/search_records) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `query.inputs.text` parameter with the query text. Pinecone uses the embedding model integrated with the index to convert the text to a dense vector automatically.
* The `query.top_k` parameter with the number of similar records to return.
* Optionally, you can specify the `fields` to return in the response. If not specified, the response will include all fields.

For example, the following code searches for the 2 records most semantically related to a query text:

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  results = index.search(
      namespace="example-namespace", 
      query={
          "inputs": {"text": "Disease prevention"}, 
          "top_k": 2
      },
      fields=["category", "chunk_text"]
  )

  print(results)
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const response = await namespace.searchRecords({
    query: {
      topK: 2,
      inputs: { text: 'Disease prevention' },
    },
    fields: ['chunk_text', 'category'],
  });

  console.log(response);
  ```

  ```java Java
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.SearchRecordsResponse;

  import java.util.*;

  public class SearchText {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "integrated-dense-java");

          String query = "Disease prevention";
          List<String> fields = new ArrayList<>();
          fields.add("category");
          fields.add("chunk_text");

          // Search the dense index
          SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 2, null, null);

          // Print the results
          System.out.println(recordsResponse);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      } 

      res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 2,
              Inputs: &map[string]interface{}{
                  "text": "Disease prevention",
              },
          },
          Fields: &[]string{"chunk_text", "category"},
      })
      if err != nil {
          log.Fatalf("Failed to search records: %v", err)
      }
      fmt.Printf(prettifyStruct(res))
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var response = await index.SearchRecordsAsync(
      "example-namespace",
      new SearchRecordsRequest
      {
          Query = new SearchRecordsRequestQuery
          {
              TopK = 4,
              Inputs = new Dictionary<string, object?> { { "text", "Disease prevention" } },
          },
          Fields = ["category", "chunk_text"],
      }
  );

  Console.WriteLine(response);
  ```

  ```shell curl
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: unstable" \
    -d '{
          "query": {
              "inputs": {"text": "Disease prevention"},
              "top_k": 2
          },
          "fields": ["category", "chunk_text"]
       }'
  ```
</CodeGroup>

The response will look as follows. Each record is returned with a similarity score that represents its distance to the query vector, calculated according to the [similarity metric](/guides/index-data/create-an-index#similarity-metrics) for the index.

<CodeGroup>
  ```python Python
  {'result': {'hits': [{'_id': 'rec3',
                        '_score': 0.8204272389411926,
                        'fields': {'category': 'immune system',
                                   'chunk_text': 'Rich in vitamin C and other '
                                                 'antioxidants, apples '
                                                 'contribute to immune health '
                                                 'and may reduce the risk of '
                                                 'chronic diseases.'}},
                       {'_id': 'rec1',
                        '_score': 0.7931625843048096,
                        'fields': {'category': 'digestive system',
                                   'chunk_text': 'Apples are a great source of '
                                                 'dietary fiber, which supports '
                                                 'digestion and helps maintain a '
                                                 'healthy gut.'}}]},
   'usage': {'embed_total_tokens': 8, 'read_units': 6}}
  ```

  ```javascript JavaScript
  {
    result: { 
      hits: [ 
        {
          _id: 'rec3',
          _score: 0.82042724,
          fields: {
            category: 'immune system',
            chunk_text: 'Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.'
          }
        },
        {
          _id: 'rec1',
          _score: 0.7931626,
          fields: {
            category: 'digestive system',
            chunk_text: 'Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.'
          }
        }
      ]
    },
    usage: { 
      readUnits: 6, 
      embedTotalTokens: 8 
    }
  }
  ```

  ```java Java
  class SearchRecordsResponse {
      result: class SearchRecordsResponseResult {
          hits: [class Hit {
              id: rec3
              score: 0.8204272389411926
              fields: {category=immune system, chunk_text=Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.}
              additionalProperties: null
          }, class Hit {
              id: rec1
              score: 0.7931625843048096
              fields: {category=endocrine system, chunk_text=Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.}
              additionalProperties: null
          }]
          additionalProperties: null
      }
      usage: class SearchUsage {
          readUnits: 6
          embedTotalTokens: 13
      }
      additionalProperties: null
  }
  ```

  ```go Go
  {
    "result": {
      "hits": [
        {
          "_id": "rec3",
          "_score": 0.82042724,
          "fields": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        {
          "_id": "rec1",
          "_score": 0.7931626,
          "fields": {
            "category": "digestive system",
            "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 8
    }
  }
  ```

  ```csharp C#
  {
      "result": {
          "hits": [
              {
                  "_id": "rec3",
                  "_score": 0.13741668,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec1",
                  "_score": 0.0023413408,
                  "fields": {
                      "category": "digestive system",
                      "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
                  }
              }
          ]
      },
      "usage": {
          "read_units": 6,
          "embed_total_tokens": 5,
          "rerank_units": 1
      }
  }
  ```

  ```json curl
   {
      "result": {
          "hits": [
              {
                  "_id": "rec3",
                  "_score": 0.82042724,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec1",
                  "_score": 0.7931626,
                  "fields": {
                      "category": "digestive system",
                      "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
                  }
              }
          ]
      },
      "usage": {
          "embed_total_tokens": 8,
          "read_units": 6
      }
  }
  ```
</CodeGroup>

## Search with a dense vector

To search a dense index with a dense vector representation of a query, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `vector` parameter with the dense vector values representing your query.
* The `top_k` parameter with the number of results to return.
* Optionally, you can set `include_values` and/or `include_metadata` to `true` to include the vector values and/or metadata of the matching records in the response. However, when querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.

For example, the following code uses a dense vector representation of the query “Disease prevention” to search for the 3 most semantically similar records in the `example-namespaces` namespace:

<CodeGroup>
  ```Python Python
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.query(
      namespace="example-namespace",
      vector=[0.0236663818359375,-0.032989501953125, ..., -0.01041412353515625,0.0086669921875], 
      top_k=3,
      include_metadata=True,
      include_values=False
  )
  ```

  ```JavaScript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      vector: [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
      topK: 3,
      includeValues: false,
      includeMetadata: true,
  });
  ```

  ```java Java
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  import java.util.Arrays;
  import java.util.List;

  public class QueryExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<Float> query = Arrays.asList(0.0236663818359375f, -0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f);
          QueryResponseWithUnsignedIndices queryResponse = index.query(3, query, null, null, null, "example-namespace", null, false, true);
          System.out.println(queryResponse);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      queryVector := []float32{0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875}

      res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
          Vector:          queryVector,
          TopK:            3,
          IncludeValues:   false,
          includeMetadata: true,
      })
      if err != nil {
          log.Fatalf("Error encountered when querying by vector: %v", err)
      } else {
          fmt.Printf(prettifyStruct(res))
      }
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Vector = new[] { 0.0236663818359375f ,-0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f },
      Namespace = "example-namespace",
      TopK = 3,
      IncludeMetadata = true,
  });

  Console.WriteLine(queryResponse);
  ```

  ```bash curl
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "vector": [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
          "namespace": "example-namespace",
          "topK": 3,
          "includeMetadata": true,
          "includeValues": false
      }'
  ```
</CodeGroup>

The response will look as follows. Each record is returned with a similarity score that represents its distance to the query vector, calculated according to the [similarity metric](/guides/index-data/create-an-index#similarity-metrics) for the index.

<CodeGroup>
  ```python Python
  {'matches': [{'id': 'rec3',
                'metadata': {'category': 'immune system',
                             'chunk_text': 'Rich in vitamin C and other '
                                            'antioxidants, apples contribute to '
                                            'immune health and may reduce the '
                                            'risk of chronic diseases.'},
                'score': 0.82026422,
                'values': []},
               {'id': 'rec1',
                'metadata': {'category': 'digestive system',
                             'chunk_text': 'Apples are a great source of '
                                            'dietary fiber, which supports '
                                            'digestion and helps maintain a '
                                            'healthy gut.'},
                'score': 0.793068111,
                'values': []},
               {'id': 'rec4',
                'metadata': {'category': 'endocrine system',
                             'chunk_text': 'The high fiber content in apples '
                                            'can also help regulate blood sugar '
                                            'levels, making them a favorable '
                                            'snack for people with diabetes.'},
                'score': 0.780169606,
                'values': []}],
   'namespace': 'example-namespace',
   'usage': {'read_units': 6}}
  ```

  ```JavaScript JavaScript
  {
    matches: [
      {
        id: 'rec3',
        score: 0.819709897,
        values: [],
        sparseValues: undefined,
        metadata: [Object]
      },
      {
        id: 'rec1',
        score: 0.792900264,
        values: [],
        sparseValues: undefined,
        metadata: [Object]
      },
      {
        id: 'rec4',
        score: 0.780068815,
        values: [],
        sparseValues: undefined,
        metadata: [Object]
      }
    ],
    namespace: 'example-namespace',
    usage: { readUnits: 6 }
  }
  ```

  ```java Java
  class QueryResponseWithUnsignedIndices {
      matches: [ScoredVectorWithUnsignedIndices {
          score: 0.8197099
          id: rec3
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "immune system"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 0.79290026
          id: rec1
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "digestive system"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 0.7800688
          id: rec4
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "endocrine system"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }]
      namespace: example-namespace
      usage: read_units: 6

  }
  ```

  ```go Go
  {
    "matches": [
      {
        "vector": {
          "id": "rec3",
          "metadata": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        "score": 0.8197099
      },
      {
        "vector": {
          "id": "rec1",
          "metadata": {
            "category": "digestive system",
            "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
          }
        },
        "score": 0.79290026
      },
      {
        "vector": {
          "id": "rec4",
          "metadata": {
            "category": "endocrine system",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
          }
        },
        "score": 0.7800688
      }
    ],
    "usage": {
      "read_units": 6
    },
    "namespace": "example-namespace"
  }
  ```

  ```csharp C#
  {
    "results": [],
    "matches": [
      {
        "id": "rec3",
        "score": 0.8197099,
        "values": [],
        "metadata": {
          "category": "immune system",
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
        }
      },
      {
        "id": "rec1",
        "score": 0.79290026,
        "values": [],
        "metadata": {
          "category": "digestive system",
          "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
        }
      },
      {
        "id": "rec4",
        "score": 0.7800688,
        "values": [],
        "metadata": {
          "category": "endocrine system",
          "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
        }
      }
    ],
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 6
    }
  }
  ```

  ```json curl
  {
      "results": [],
      "matches": [
          {
              "id": "rec3",
              "score": 0.820593238,
              "values": [],
              "metadata": {
                  "category": "immune system",
                  "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
              }
          },
          {
              "id": "rec1",
              "score": 0.792266726,
              "values": [],
              "metadata": {
                  "category": "digestive system",
                  "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
              }
          },
          {
              "id": "rec4",
              "score": 0.780045748,
              "values": [],
              "metadata": {
                  "category": "endocrine system",
                  "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
              }
          }
      ],
      "namespace": "example-namespace",
      "usage": {
          "readUnits": 6
      }
  }
  ```
</CodeGroup>

## Search with a record ID

When you search with a record ID, Pinecone uses the dense vector associated with the record as the query. To search a dense index with a record ID, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `id` parameter with the unique record ID containing the vector to use as the query.
* The `top_k` parameter with the number of results to return.
* Optionally, you can set `include_values` and/or `include_metadata` to `true` to include the vector values and/or metadata of the matching records in the response. However, when querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.

For example, the following code uses an ID to search for the 3 records in the `example-namespace` namespace that are most semantically similar to the dense vector in the record:

<CodeGroup>
  ```Python Python
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.query(
      namespace="example-namespace",
      id="rec2", 
      top_k=3,
      include_metadata=True,
      include_values=False
  )
  ```

  ```JavaScript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      id: 'rec2',
      topK: 3,
      includeValues: false,
      includeMetadata: true,
  });
  ```

  ```java Java
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  public class QueryExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          QueryResponseWithUnsignedIndices queryRespone = index.queryByVectorId(3, "rec2", "example-namespace", null, false, true);
          System.out.println(queryResponse);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      vectorId := "rec2"
      res, err := idxConnection.QueryByVectorId(ctx, &pinecone.QueryByVectorIdRequest{
          VectorId:      vectorId,
          TopK:          3,
          IncludeValues: false,
          IncludeMetadata: true,
      })
      if err != nil {
          log.Fatalf("Error encountered when querying by vector ID `%v`: %v", vectorId, err)
      } else {
          fmt.Printf(prettifyStruct(res.Matches))
      }
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Id = "rec2",
      Namespace = "example-namespace",
      TopK = 3,
      IncludeValues = false,
      IncludeMetadata = true
  });

  Console.WriteLine(queryResponse);
  ```

  ```bash curl
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "id": "rec2",
          "namespace": "example-namespace",
          "topK": 3,
          "includeMetadata": true,
          "includeValues": false
      }'
  ```
</CodeGroup>

## Parallel queries

Python SDK v6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Async support makes it possible to use Pinecone with modern async web frameworks such as FastAPI, Quart, and Sanic, and can significantly increase the efficiency of running queries in parallel. For more details, see the [Async requests](/reference/python-sdk#async-requests).

# Lexical search

This page shows you how to search a [sparse index](/guides/index-data/indexing-overview#sparse-indexes) for records that most exactly match the words or phrases in a query. This is often called lexical search or keyword search.

Lexical search uses [sparse vectors](https://www.pinecone.io/learn/sparse-retrieval/), which have a very large number of dimensions, where only a small proportion of values are non-zero. The dimensions represent words from a dictionary, and the values represent the importance of these words in the document. Words are scored independently and then summed, with the most similar records scored highest.

## Search with text

<Note>
  Searching with text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
</Note>

To search a sparse index with a query text, use the [`search_records`](/reference/api/latest/data-plane/search_records) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `query.inputs.text`:  The query text. Pinecone uses the [embedding model](/guides/index-data/create-an-index#embedding-models) integrated with the index to convert the text to a sparse vector automatically.
* `query.top_k`:  The number of records to return.
* `query.match_terms`: (Optional) A list of terms that must be present in each search result. For more details, see [Filter by required terms](#filter-by-required-terms).
* `fields`: (Optional) The fields to return in the response. If not specified, the response includes all fields.

For example, the following code converts the query “What is AAPL's outlook, considering both product launches and market conditions?” to a sparse vector and then searches for the 3 most similar vectors in the `example-namespace` namespace:

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  results = index.search(
      namespace="example-namespace", 
      query={
          "inputs": {"text": "What is AAPL's outlook, considering both product launches and market conditions?"}, 
          "top_k": 3
      },
      fields=["chunk_text", "quarter"]
  )

  print(results)
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const response = await namespace.searchRecords({
    query: {
      topK: 3,
      inputs: { text: "What is AAPL's outlook, considering both product launches and market conditions?" },
    },
    fields: ['chunk_text', 'quarter']
  });

  console.log(response);
  ```

  ```java Java
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.SearchRecordsResponse;

  import java.util.*;

  public class SearchText {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "integrated-sparse-java");

          String query = "What is AAPL's outlook, considering both product launches and market conditions?";
          List<String> fields = new ArrayList<>();
          fields.add("category");
          fields.add("chunk_text");

          // Search the sparse index
          SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 3, null, null);

          // Print the results
          System.out.println(recordsResponse);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      } 

      res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 3,
              Inputs: &map[string]interface{}{
                  "text": "What is AAPL's outlook, considering both product launches and market conditions?",
              },
          },
          Fields: &[]string{"chunk_text", "category"},
      })
      if err != nil {
          log.Fatalf("Failed to search records: %v", err)
      }
      fmt.Printf(prettifyStruct(res))
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var response = await index.SearchRecordsAsync(
      "example-namespace",
      new SearchRecordsRequest
      {
          Query = new SearchRecordsRequestQuery
          {
              TopK = 3,
              Inputs = new Dictionary<string, object?> { { "text", "What is AAPL's outlook, considering both product launches and market conditions?" } },
          },
          Fields = ["category", "chunk_text"],
      }
  );

  Console.WriteLine(response);
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/records/namespaces/example-namespace/search" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "query": {
            "inputs": { "text": "What is AAPL'\''s outlook, considering both product launches and market conditions?" },
            "top_k": 3
          },
          "fields": ["chunk_text", "quarter"]
      }'
  ```
</CodeGroup>

The results will look as follows. The most similar records are scored highest.

<CodeGroup>
  ```python Python
  {'result': {'hits': [{'_id': 'vec2',
                        '_score': 10.77734375,
                        'fields': {'chunk_text': "Analysts suggest that AAPL'''s "
                                                 'upcoming Q4 product launch '
                                                 'event might solidify its '
                                                 'position in the premium '
                                                 'smartphone market.',
                                   'quarter': 'Q4'}},
                       {'_id': 'vec3',
                        '_score': 6.49066162109375,
                        'fields': {'chunk_text': "AAPL'''s strategic Q3 "
                                                 'partnerships with '
                                                 'semiconductor suppliers could '
                                                 'mitigate component risks and '
                                                 'stabilize iPhone production.',
                                   'quarter': 'Q3'}},
                       {'_id': 'vec1',
                        '_score': 5.3671875,
                        'fields': {'chunk_text': 'AAPL reported a year-over-year '
                                                 'revenue increase, expecting '
                                                 'stronger Q3 demand for its '
                                                 'flagship phones.',
                                   'quarter': 'Q3'}}]},
   'usage': {'embed_total_tokens': 18, 'read_units': 1}}
  ```

  ```javascript JavaScript
  {
    result: { 
      hits: [ 
        {
          _id: "vec2",
          _score: 10.82421875,
          fields: {
            chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
            quarter: "Q4"
          }
        },
        {
          _id: "vec3",
          _score: 6.49066162109375,
          fields: {
            chunk_text: "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
            quarter: "Q3"
          }
        },
        {
          _id: "vec1",
          _score: 5.3671875,
          fields: {
            chunk_text: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            quarter: "Q3"
          }
        }
      ]
    },
    usage: { 
      readUnits: 1, 
      embedTotalTokens: 18 
    }
  }
  ```

  ```java Java
  class SearchRecordsResponse {
      result: class SearchRecordsResponseResult {
          hits: [class Hit {
              id: vec2
              score: 10.82421875
              fields: {chunk_text=Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market., quarter=Q4}
              additionalProperties: null
          }, class Hit {
              id: vec3
              score: 6.49066162109375
              fields: {chunk_text=AAAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production., quarter=Q3}
              additionalProperties: null
          }, class Hit {
              id: vec1
              score: 5.3671875
              fields: {chunk_text=AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones., quarter=Q3}
              additionalProperties: null
          }]
          additionalProperties: null
      }
      usage: class SearchUsage {
          readUnits: 1
          embedTotalTokens: 18
      }
      additionalProperties: null
  }
  ```

  ```go Go
  {
    "result": {
      "hits": [
        {
          "_id": "vec2",
          "_score": 10.833984,
          "fields": {
            "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
            "quarter": "Q4"
          }
        },
        {
          "_id": "vec3",
          "_score": 6.473572,
          "fields": {
            "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
            "quarter": "Q3"
          }
        },
        {
          "_id": "vec1",
          "_score": 5.3710938,
          "fields": {
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            "quarter": "Q3"
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 18
    }
  }
  ```

  ```csharp C#
  {
      "result": {
          "hits": [
              {
                  "_id": "vec2",
                  "_score": 10.833984,
                  "fields": {
                      "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                      "quarter": "Q4"
                  }
              },
              {
                  "_id": "vec3",
                  "_score": 6.473572,
                  "fields": {
                      "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
                      "quarter": "Q3"
                  }
              },
              {
                  "_id": "vec1",
                  "_score": 5.3710938,
                  "fields": {
                      "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                      "quarter": "Q3"
                  }
              }
          ]
      },
      "usage": {
          "read_units": 6,
          "embed_total_tokens": 18
      }
  }
  ```

  ```json curl
  {
    "result": {
      "hits": [
        {
          "_id": "vec2",
          "_score": 10.82421875,
          "fields": {
            "chunk_text": "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
            "quarter": "Q4"
          }
        },
        {
          "_id": "vec3",
          "_score": 6.49066162109375,
          "fields": {
            "chunk_text": "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
            "quarter": "Q3"
          }
        },
        {
          "_id": "vec1",
          "_score": 5.3671875,
          "fields": {
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            "quarter": "Q3"
          }
        }
      ]
    },
    "usage": {
      "embed_total_tokens": 18,
      "read_units": 1
    }
  }
  ```
</CodeGroup>

## Search with a sparse vector

To search a sparse index with a sparse vector representation of a query, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `sparse_vector`: The sparse vector values and indices.
* `top_k`: The number of results to return.
* `include_values`: Whether to include the vector values of the matching records in the response. Defaults to `false`.
* `include_metadata`: Whether to include the metadata of the matching records in the response. Defaults to `false`.
  <Note>
    When querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.
  </Note>

For example, the following code uses a sparse vector representation of the query "What is AAPL's outlook, considering both product launches and market conditions?" to search for the 3 most similar vectors in the `example-namespace` namespace:

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  results = index.query(
      namespace="example-namespace",
      sparse_vector={
        "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
      }, 
      top_k=3,
      include_metadata=True,
      include_values=False
  )

  print(results)
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      sparseVector: {
          indices: [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697],
          values: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
      },
      topK: 3,
      includeValues: false,
      includeMetadata: true
  });

  console.log(queryResponse);
  ```

  ```java Java
  import io.pinecone.clients.Pinecone;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;
  import io.pinecone.clients.Index;

  import java.util.*;

  public class SearchSparseIndex {
      public static void main(String[] args) throws InterruptedException {
          // Instantiate Pinecone class
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";

          Index index = pinecone.getIndexConnection(indexName);

          List<Long> sparseIndices = Arrays.asList(
                  767227209L, 1640781426L, 1690623792L, 2021799277L, 2152645940L,
                  2295025838L, 2443437770L, 2779594451L, 2956155693L, 3476647774L,
                  3818127854L, 428309169L);
          List<Float> sparseValues = Arrays.asList(
                  1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
                  1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f);

          QueryResponseWithUnsignedIndices queryResponse = index.query(3, null, sparseIndices, sparseValues, null, "example-namespace", null, false, true);
          System.out.println(queryResponse);
      }
  }
  ```

  ```go Go
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	// To get the unique host for an index,
  	// see https://docs.pinecone.io/guides/manage-data/target-an-index
  	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
  	if err != nil {
  		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

  	sparseValues := pinecone.SparseValues{
  		Indices: []uint32{767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697},
  		Values:  []float32{1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0},
  	}

  	res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
  		SparseValues:    &sparseValues,
  		TopK:            3,
  		IncludeValues:   false,
  		IncludeMetadata: true,
  	})
  	if err != nil {
  		log.Fatalf("Error encountered when querying by vector: %v", err)
  	} else {
  		fmt.Printf(prettifyStruct(res))
  	}
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  var index = pinecone.Index("docs-example");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Namespace = "example-namespace",
      TopK = 4,
      SparseVector = new SparseValues
      {
          Indices = [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697],
          Values = new[] { 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f },
      },
      IncludeValues = false,
      IncludeMetadata = true
  });

  Console.WriteLine(queryResponse);
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "sparseVector": {
              "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
              "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
          },
          "namespace": "example-namespace",
          "topK": 4,
          "includeMetadata": true,
          "includeValues": false
      }'
  ```
</CodeGroup>

The results will look as follows. The most similar records are scored highest.

<CodeGroup>
  ```python Python
  {'matches': [{'id': 'vec2',
                'metadata': {'category': 'technology',
                             'quarter': 'Q4',
                             'chunk_text': "Analysts suggest that AAPL'''s "
                                            'upcoming Q4 product launch event '
                                            'might solidify its position in the '
                                            'premium smartphone market.'},
                'score': 10.9042969,
                'values': []},
               {'id': 'vec3',
                'metadata': {'category': 'technology',
                             'quarter': 'Q3',
                             'chunk_text': "AAPL'''s strategic Q3 partnerships "
                                            'with semiconductor suppliers could '
                                            'mitigate component risks and '
                                            'stabilize iPhone production'},
                'score': 6.48010254,
                'values': []},
               {'id': 'vec1',
                'metadata': {'category': 'technology',
                             'quarter': 'Q3',
                             'chunk_text': 'AAPL reported a year-over-year '
                                            'revenue increase, expecting '
                                            'stronger Q3 demand for its flagship '
                                            'phones.'},
                'score': 5.3671875,
                'values': []}],
   'namespace': 'example-namespace',
   'usage': {'read_units': 1}}
  ```

  ```javascript JavaScript
  { 
    matches: [
              { 
                id: 'vec2',
                score: 10.9042969,
                values: [],
                metadata: {
                  chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                  category: 'technology',
                  quarter: 'Q4'
                }
              },
              {
                id: 'vec3',
                score: 6.48010254,
                values: [],
                metadata: {
                  chunk_text: "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
                  category: 'technology',
                  quarter: 'Q3'
                }
              },
              {
                id: 'vec1',
                score: 5.3671875,
                values: [],
                metadata: {
                    chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.',
                    category: 'technology',
                    quarter: 'Q3'
                }
              }
            ],
    namespace: 'example-namespace',
    usage: {readUnits: 1}
  }
  ```

  ```java Java
  class QueryResponseWithUnsignedIndices {
      matches: [ScoredVectorWithUnsignedIndices {
          score: 10.34375
          id: vec2
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "technology"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "Analysts suggest that AAPL\'\\\'\'s upcoming Q4 product launch event might solidify its position in the premium smartphone market."
            }
          }
          fields {
            key: "quarter"
            value {
              string_value: "Q4"
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 5.8638916
          id: vec3
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "technology"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "AAPL\'\\\'\'s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"
            }
          }
          fields {
            key: "quarter"
            value {
              string_value: "Q3"
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }, ScoredVectorWithUnsignedIndices {
          score: 5.3671875
          id: vec1
          values: []
          metadata: fields {
            key: "category"
            value {
              string_value: "technology"
            }
          }
          fields {
            key: "chunk_text"
            value {
              string_value: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
            }
          }
          fields {
            key: "quarter"
            value {
              string_value: "Q3"
            }
          }
          
          sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
              indicesWithUnsigned32Int: []
              values: []
          }
      }]
      namespace: example-namespace
      usage: read_units: 1

  }
  ```

  ```go Go
  {
    "matches": [
      {
        "vector": {
          "id": "vec2",
          "metadata": {
            "category": "technology",
            "quarter": "Q4",
            "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
          }
        },
        "score": 10.904296
      },
      {
        "vector": {
          "id": "vec3",
          "metadata": {
            "category": "technology",
            "quarter": "Q3",
            "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"
          }
        },
        "score": 6.4801025
      },
      {
        "vector": {
          "id": "vec1",
          "metadata": {
            "category": "technology",
            "quarter": "Q3",
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones"
          }
        },
        "score": 5.3671875
      }
    ],
    "usage": {
      "read_units": 1
    },
    "namespace": "example-namespace"
  }
  ```

  ```csharp C#
  {
    "results": [],
    "matches": [
      {
        "id": "vec2",
        "score": 10.904297,
        "values": [],
        "metadata": {
          "category": "technology",
          "chunk_text": "Analysts suggest that AAPL\u0027\u0027\u0027s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "quarter": "Q4"
        }
      },
      {
        "id": "vec3",
        "score": 6.4801025,
        "values": [],
        "metadata": {
          "category": "technology",
          "chunk_text": "AAPL\u0027\u0027\u0027s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
          "quarter": "Q3"
        }
      },
      {
        "id": "vec1",
        "score": 5.3671875,
        "values": [],
        "metadata": {
          "category": "technology",
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          "quarter": "Q3"
        }
      }
    ],
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```

  ```json curl
  {
    "results": [],
    "matches": [
      {
        "id": "vec2",
        "score": 10.9042969,
        "values": [],
        "metadata": {
          "chunk_text": "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "category": "technology",
          "quarter": "Q4"
        }
      },
      {
        "id": "vec3",
        "score": 6.48010254,
        "values": [],
        "metadata": {
          "chunk_text": "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
          "category": "technology",
          "quarter": "Q3"
        }
      },
      {
        "id": "vec1",
        "score": 5.3671875,
        "values": [],
        "metadata": {
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            "category": "technology",
            "quarter": "Q3"
        }
      }
    ],
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```
</CodeGroup>

## Search with a record ID

When you search with a record ID, Pinecone uses the sparse vector associated with the record as the query. To search a sparse index with a record ID, use the [`query`](/reference/api/latest/data-plane/query) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `id`: The unique record ID containing the sparse vector to use as the query.
* `top_k`: The number of results to return.
* `include_values`: Whether to include the vector values of the matching records in the response. Defaults to `false`.
* `include_metadata`: Whether to include the metadata of the matching records in the response. Defaults to `false`.
  <Note>
    When querying with `top_k` over 1000, avoid returning vector data or metadata for optimal performance.
  </Note>

For example, the following code uses an ID to search for the 3 records in the `example-namespace` namespace that best match the sparse vector in the record:

<CodeGroup>
  ```Python Python
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.query(
      namespace="example-namespace",
      id="rec2", 
      top_k=3,
      include_metadata=True,
      include_values=False
  )
  ```

  ```JavaScript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const queryResponse = await index.namespace('example-namespace').query({
      id: 'rec2',
      topK: 3,
      includeValues: false,
      includeMetadata: true,
  });
  ```

  ```java Java
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

  public class QueryExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          QueryResponseWithUnsignedIndices queryRespone = index.queryByVectorId(3, "rec2", "example-namespace", null, false, true);
          System.out.println(queryResponse);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      vectorId := "rec2"
      res, err := idxConnection.QueryByVectorId(ctx, &pinecone.QueryByVectorIdRequest{
          VectorId:      vectorId,
          TopK:          3,
          IncludeValues: false,
          IncludeMetadata: true,
      })
      if err != nil {
          log.Fatalf("Error encountered when querying by vector ID `%v`: %v", vectorId, err)
      } else {
          fmt.Printf(prettifyStruct(res.Matches))
      }
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var queryResponse = await index.QueryAsync(new QueryRequest {
      Id = "rec2",
      Namespace = "example-namespace",
      TopK = 3,
      IncludeValues = false,
      IncludeMetadata = true
  });

  Console.WriteLine(queryResponse);
  ```

  ```bash curl
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
          "id": "rec2",
          "namespace": "example-namespace",
          "topK": 3,
          "includeMetadata": true,
          "includeValues": false
      }'
  ```
</CodeGroup>

## Filter by required terms

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and is available only on the `2025-10` version of the API. See [limitations](#limitations) for details.
</Note>

When [searching with text](#search-with-text), you can specify a list of terms that must be present in each lexical search result. This is especially useful for:

* **Precision filtering**: Ensuring specific entities or concepts appear in results
* **Quality control**: Filtering out results that don't contain essential keywords
* **Domain-specific searches**: Requiring domain-specific terminology in results
* **Entity-based filtering**: Ensuring specific people, places, or things are mentioned

To filter by required terms, add `match_terms` to your query, specifying the `terms` to require and the `strategy` to use. Currently, `all` is the only strategy supported (all terms must be present).

For example, the following request searches for records about Tesla's stock performance while ensuring both "Tesla" and "stock" appear in each result:

```bash curl
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/records/namespaces/example-namespace/search" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-API-Version: unstable" \
  -d '{
        "query": {
          "inputs": { "text": "What is the current outlook for Tesla stock performance?" },
          "top_k": 3,
          "match_terms": {
            "terms": ["Tesla", "stock"],
            "strategy": "all"
          }
        },
        "fields": ["chunk_text"]
    }'
```

The response includes only records that contain both "Tesla" and "stock":

```json
{
  "result": {
    "hits": [
      {
        "_id": "tesla_q4_earnings",
        "_score": 9.82421875,
        "fields": {
          "chunk_text": "Tesla stock surged 8% in after-hours trading following strong Q4 earnings that exceeded analyst expectations. The company reported record vehicle deliveries and improved profit margins."
        }
      },
      {
        "_id": "tesla_competition_analysis",
        "_score": 7.49066162109375,
        "fields": {
          "chunk_text": "Tesla stock faces increasing competition from traditional automakers entering the electric vehicle market. However, analysts maintain that Tesla's technological lead and brand recognition provide significant advantages."
        }
      },
      {
        "_id": "tesla_production_update",
        "_score": 6.3671875,
        "fields": {
          "chunk_text": "Tesla stock performance is closely tied to production capacity at its Gigafactories. Recent expansion announcements suggest the company is positioning for continued growth in global markets."
        }
      }
    ]
  },
  "usage": {
    "embed_total_tokens": 18,
    "read_units": 1
  }
}
```

Without the `match_terms` filter, you might get results like:

* "Tesla cars are popular in California" (mentions Tesla but not stock)
* "Stock market volatility affects tech companies" (mentions stock but not Tesla)
* "Electric vehicle sales are growing" (neither Tesla nor stock)

### Limitations

* **Integrated indexes only**: Filtering by required terms is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
* **Post-processing filter**: The filtering happens after the initial query, so potential matches that weren't included in the initial `top_k` results won't appear in the final results
* **No phrase matching**: Terms are matched individually in any order and location.
* **No case-sensitivity**: Terms are normalized during processing.

# Hybrid search

[Semantic search](/guides/search/semantic-search) and [lexical search](/guides/search/lexical-search) are powerful information retrieval techniques, but each has notable limitations. For example, semantic search can miss results based on exact keyword matches, especially in scenarios involving domain-specific terminology, while lexical search can miss results based on relationships, such as synonyms and paraphrases.

This page shows you how to lift these limitations by combining semantic and lexical search. This is often called hybrid search.

## Hybrid search approaches

There are two ways to perform hybrid search in Pinecone:

* [Use separate dense and sparse indexes](#use-separate-dense-and-sparse-indexes). This is the **recommended** approach because it provides the most flexibility.
* [Use a single hybrid index](#use-a-single-hybrid-index). This approach is simpler to implement but doesn't support a few useful features.

The following table summarizes the pros and cons between the two approaches:

| Approach                          | Pros                                                                                                                                                                                                                                                                                       | Cons                                                                                                                                                                            |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Separate dense and sparse indexes | <ul><li>You can start with dense for semantic search and add sparse for lexical search later.</li><li>You can do sparse-only queries.</li><li>You can rerank at multiple levels (for each index and for merged results).</li><li>You can use integrated embedding and reranking.</li></ul> | <ul><li>You need to manage and make requests to two separate indexes.</li><li>You need to maintain the linkage between sparse and dense vectors in different indexes.</li></ul> |
| Single hybrid index               | <ul><li>You make requests to only a single index.</li><li>The linkage between dense and sparse vectors is implicit.</li></ul>                                                                                                                                                              | <ul><li>You can't do sparse-only queries.</li><li>You can't use integrated embedding and reranking.</li></ul>                                                                   |

## Use separate dense and sparse indexes

This is the recommended way to perform hybrid search in Pinecone. You create separate dense and sparse indexes, upsert dense vectors into the dense index and sparse vectors into the sparse index, and search each index separately. Then you combine and deduplicate the results, use one of Pinecone's [hosted reranking models](/guides/search/rerank-results#reranking-models) to rerank them based on a unified relevance score, and return the most relevant matches.

<Steps>
  <Step title="Create dense and sparse indexes">
    [Create a dense index](/guides/index-data/create-an-index#create-a-dense-index) and [create a sparse index](/guides/index-data/create-an-index#create-a-sparse-index), either with integrated embedding or for vectors created with external models.

    For example, the following code creates indexes with integrated embedding models.

    ```python Python
    from pinecone import Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    dense_index_name = "dense-for-hybrid-py"
    sparse_index_name = "sparse-for-hybrid-py"

    if not pc.has_index(dense_index_name):
        pc.create_index_for_model(
            name=dense_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"llama-text-embed-v2",
                "field_map":{"text": "chunk_text"}
            }
        )

    if not pc.has_index(sparse_index_name):
        pc.create_index_for_model(
            name=sparse_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"pinecone-sparse-english-v0",
                "field_map":{"text": "chunk_text"}
            }
        )
    ```
  </Step>

  <Step title="Upsert dense and sparse vectors">
    [Upsert dense vectors](/guides/index-data/upsert-data#upsert-dense-vectors) into the dense index and [upsert sparse vectors](/guides/index-data/upsert-data#upsert-sparse-vectors) into the sparse index.

    Make sure to establish a linkage between the dense and sparse vectors so you can merge and deduplicate search results later. For example, the following uses `_id` as the linkage, but you can use any other custom field as well. Because the indexes are integrated with embedding models, you provide the source texts and Pinecone converts them to vectors automatically.

    ```python Python [expandable]
    # Define the records
    records = [
        { "_id": "vec1", "chunk_text": "Apple Inc. issued a $10 billion corporate bond in 2023." },
        { "_id": "vec2", "chunk_text": "ETFs tracking the S&P 500 outperformed active funds last year." },
        { "_id": "vec3", "chunk_text": "Tesla's options volume surged after the latest earnings report." },
        { "_id": "vec4", "chunk_text": "Dividend aristocrats are known for consistently raising payouts." },
        { "_id": "vec5", "chunk_text": "The Federal Reserve raised interest rates by 0.25% to curb inflation." },
        { "_id": "vec6", "chunk_text": "Unemployment hit a record low of 3.7% in Q4 of 2024." },
        { "_id": "vec7", "chunk_text": "The CPI index rose by 6% in July 2024, raising concerns about purchasing power." },
        { "_id": "vec8", "chunk_text": "GDP growth in emerging markets outpaced developed economies." },
        { "_id": "vec9", "chunk_text": "Amazon's acquisition of MGM Studios was valued at $8.45 billion." },
        { "_id": "vec10", "chunk_text": "Alphabet reported a 20% increase in advertising revenue." },
        { "_id": "vec11", "chunk_text": "ExxonMobil announced a special dividend after record profits." },
        { "_id": "vec12", "chunk_text": "Tesla plans a 3-for-1 stock split to attract retail investors." },
        { "_id": "vec13", "chunk_text": "Credit card APRs reached an all-time high of 22.8% in 2024." },
        { "_id": "vec14", "chunk_text": "A 529 college savings plan offers tax advantages for education." },
        { "_id": "vec15", "chunk_text": "Emergency savings should ideally cover 6 months of expenses." },
        { "_id": "vec16", "chunk_text": "The average mortgage rate rose to 7.1% in December." },
        { "_id": "vec17", "chunk_text": "The SEC fined a hedge fund $50 million for insider trading." },
        { "_id": "vec18", "chunk_text": "New ESG regulations require companies to disclose climate risks." },
        { "_id": "vec19", "chunk_text": "The IRS introduced a new tax bracket for high earners." },
        { "_id": "vec20", "chunk_text": "Compliance with GDPR is mandatory for companies operating in Europe." },
        { "_id": "vec21", "chunk_text": "What are the best-performing green bonds in a rising rate environment?" },
        { "_id": "vec22", "chunk_text": "How does inflation impact the real yield of Treasury bonds?" },
        { "_id": "vec23", "chunk_text": "Top SPAC mergers in the technology sector for 2024." },
        { "_id": "vec24", "chunk_text": "Are stablecoins a viable hedge against currency devaluation?" },
        { "_id": "vec25", "chunk_text": "Comparison of Roth IRA vs 401(k) for high-income earners." },
        { "_id": "vec26", "chunk_text": "Stock splits and their effect on investor sentiment." },
        { "_id": "vec27", "chunk_text": "Tech IPOs that disappointed in their first year." },
        { "_id": "vec28", "chunk_text": "Impact of interest rate hikes on bank stocks." },
        { "_id": "vec29", "chunk_text": "Growth vs. value investing strategies in 2024." },
        { "_id": "vec30", "chunk_text": "The role of artificial intelligence in quantitative trading." },
        { "_id": "vec31", "chunk_text": "What are the implications of quantitative tightening on equities?" },
        { "_id": "vec32", "chunk_text": "How does compounding interest affect long-term investments?" },
        { "_id": "vec33", "chunk_text": "What are the best assets to hedge against inflation?" },
        { "_id": "vec34", "chunk_text": "Can ETFs provide better diversification than mutual funds?" },
        { "_id": "vec35", "chunk_text": "Unemployment hit at 2.4% in Q3 of 2024." },
        { "_id": "vec36", "chunk_text": "Unemployment is expected to hit 2.5% in Q3 of 2024." },
        { "_id": "vec37", "chunk_text": "In Q3 2025 unemployment for the prior year was revised to 2.2%"},
        { "_id": "vec38", "chunk_text": "Emerging markets witnessed increased foreign direct investment as global interest rates stabilized." },
        { "_id": "vec39", "chunk_text": "The rise in energy prices significantly impacted inflation trends during the first half of 2024." },
        { "_id": "vec40", "chunk_text": "Labor market trends show a declining participation rate despite record low unemployment in 2024." },
        { "_id": "vec41", "chunk_text": "Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand." },
        { "_id": "vec42", "chunk_text": "Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries." },
        { "_id": "vec43", "chunk_text": "The U.S. dollar weakened against a basket of currencies as the global economy adjusted to shifting trade balances." },
        { "_id": "vec44", "chunk_text": "Central banks worldwide increased gold reserves to hedge against geopolitical and economic instability." },
        { "_id": "vec45", "chunk_text": "Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations." },
        { "_id": "vec46", "chunk_text": "Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects." },
        { "_id": "vec47", "chunk_text": "The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand." },
        { "_id": "vec48", "chunk_text": "Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024." },
        { "_id": "vec49", "chunk_text": "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports." },
        { "_id": "vec50", "chunk_text": "AI-driven automation in the manufacturing sector boosted productivity but raised concerns about job displacement." },
        { "_id": "vec51", "chunk_text": "The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth." },
        { "_id": "vec52", "chunk_text": "Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change." },
        { "_id": "vec53", "chunk_text": "Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization." },
        { "_id": "vec54", "chunk_text": "The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks." },
        { "_id": "vec55", "chunk_text": "Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows." },
        { "_id": "vec56", "chunk_text": "Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession." },
        { "_id": "vec57", "chunk_text": "Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth." },
        { "_id": "vec58", "chunk_text": "Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies." },
        { "_id": "vec59", "chunk_text": "The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks." },
        { "_id": "vec60", "chunk_text": "Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness." },
        { "_id": "vec61", "chunk_text": "The World Bank reported declining poverty rates globally, but regional disparities persisted." },
        { "_id": "vec62", "chunk_text": "Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities." },
        { "_id": "vec63", "chunk_text": "Population aging emerged as a critical economic issue in 2024, especially in advanced economies." },
        { "_id": "vec64", "chunk_text": "Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials." },
        { "_id": "vec65", "chunk_text": "The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand." },
        { "_id": "vec66", "chunk_text": "Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship." },
        { "_id": "vec67", "chunk_text": "Renewable energy projects accounted for a record share of global infrastructure investment in 2024." },
        { "_id": "vec68", "chunk_text": "Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure." },
        { "_id": "vec69", "chunk_text": "The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs." },
        { "_id": "vec70", "chunk_text": "Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods." },
        { "_id": "vec71", "chunk_text": "The economic impact of the 2008 financial crisis was mitigated by quantitative easing policies." },
        { "_id": "vec72", "chunk_text": "In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe." },
        { "_id": "vec73", "chunk_text": "The historical relationship between inflation and unemployment is explained by the Phillips Curve." },
        { "_id": "vec74", "chunk_text": "The World Trade Organization's role in resolving disputes was tested in 2024." },
        { "_id": "vec75", "chunk_text": "The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024." },
        { "_id": "vec76", "chunk_text": "The cost of living crisis has been exacerbated by stagnant wage growth and rising inflation." },
        { "_id": "vec77", "chunk_text": "Supply chain resilience became a top priority for multinational corporations in 2024." },
        { "_id": "vec78", "chunk_text": "Consumer sentiment surveys in 2024 reflected optimism despite high interest rates." },
        { "_id": "vec79", "chunk_text": "The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains." },
        { "_id": "vec80", "chunk_text": "Technological innovation in the fintech sector disrupted traditional banking in 2024." },
        { "_id": "vec81", "chunk_text": "The link between climate change and migration patterns is increasingly recognized." },
        { "_id": "vec82", "chunk_text": "Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels." },
        { "_id": "vec83", "chunk_text": "The economic fallout of geopolitical tensions was evident in rising defense budgets worldwide." },
        { "_id": "vec84", "chunk_text": "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets." },
        { "_id": "vec85", "chunk_text": "Declining birth rates in advanced economies pose long-term challenges for labor markets." },
        { "_id": "vec86", "chunk_text": "Digital transformation initiatives in 2024 drove productivity gains in the services sector." },
        { "_id": "vec87", "chunk_text": "The U.S. labor market's resilience in 2024 defied predictions of a severe recession." },
        { "_id": "vec88", "chunk_text": "New fiscal measures in the European Union aimed to stabilize debt levels post-pandemic." },
        { "_id": "vec89", "chunk_text": "Venture capital investments in 2024 leaned heavily toward AI and automation startups." },
        { "_id": "vec90", "chunk_text": "The surge in e-commerce in 2024 was facilitated by advancements in logistics technology." },
        { "_id": "vec91", "chunk_text": "The impact of ESG investing on corporate strategies has been a major focus in 2024." },
        { "_id": "vec92", "chunk_text": "Income inequality widened in 2024 despite strong economic growth in developed nations." },
        { "_id": "vec93", "chunk_text": "The collapse of FTX highlighted the volatility and risks associated with cryptocurrencies." },
        { "_id": "vec94", "chunk_text": "Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending." },
        { "_id": "vec95", "chunk_text": "Automation in agriculture in 2024 increased yields but displaced rural workers." },
        { "_id": "vec96", "chunk_text": "New trade agreements signed 2022 will make an impact in 2024"},
    ]
    ```

    ```python Python
    # Target the dense and sparse indexes
    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    dense_index = pc.Index(host="INDEX_HOST")
    sparse_index = pc.Index(host="INDEX_HOST")

    # Upsert the records
    # The `chunk_text` fields are converted to dense and sparse vectors
    dense_index.upsert_records("example-namespace", records)
    sparse_index.upsert_records("example-namespace", records)
    ```
  </Step>

  <Step title="Search the dense index">
    Perform a [semantic search](/guides/search/semantic-search) on the dense index.

    For example, the following code searches the dense index for 40 records most semantically related to the query "Q3 2024 us economic data". Because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a dense vector automatically.

    ```python Python
    query = "Q3 2024 us economic data"

    dense_results = dense_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(dense_results)
    ```

    ```python Response [expandable]
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 0.8629686832427979,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec36',
                          '_score': 0.8573639988899231,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec6',
                          '_score': 0.8535352945327759,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 0.8336166739463806,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec48',
                          '_score': 0.8328524827957153,
                          'fields': {'chunk_text': 'Wage growth outpaced inflation '
                                                   'for the first time in years, '
                                                   'signaling improved purchasing '
                                                   'power in 2024.'}},
                         {'_id': 'vec55',
                          '_score': 0.8322604298591614,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec45',
                          '_score': 0.8309446573257446,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec72',
                          '_score': 0.8275909423828125,
                          'fields': {'chunk_text': 'In early 2024, global GDP '
                                                   'growth slowed, driven by '
                                                   'weaker exports in Asia and '
                                                   'Europe.'}},
                         {'_id': 'vec29',
                          '_score': 0.8270887136459351,
                          'fields': {'chunk_text': 'Growth vs. value investing '
                                                   'strategies in 2024.'}},
                         {'_id': 'vec46',
                          '_score': 0.8263787627220154,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec79',
                          '_score': 0.8258304595947266,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec87',
                          '_score': 0.8257324695587158,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec40',
                          '_score': 0.8253997564315796,
                          'fields': {'chunk_text': 'Labor market trends show a '
                                                   'declining participation rate '
                                                   'despite record low '
                                                   'unemployment in 2024.'}},
                         {'_id': 'vec37',
                          '_score': 0.8235862255096436,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec58',
                          '_score': 0.8233317136764526,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec47',
                          '_score': 0.8231339454650879,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec41',
                          '_score': 0.8187897801399231,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec56',
                          '_score': 0.8155254125595093,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}},
                         {'_id': 'vec63',
                          '_score': 0.8136948347091675,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec52',
                          '_score': 0.8129132390022278,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec23',
                          '_score': 0.8126378655433655,
                          'fields': {'chunk_text': 'Top SPAC mergers in the '
                                                   'technology sector for 2024.'}},
                         {'_id': 'vec62',
                          '_score': 0.8116977214813232,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec64',
                          '_score': 0.8109902739524841,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec54',
                          '_score': 0.8092231154441833,
                          'fields': {'chunk_text': 'The global tourism sector '
                                                   'showed signs of recovery in '
                                                   'late 2024 after years of '
                                                   'pandemic-related setbacks.'}},
                         {'_id': 'vec96',
                          '_score': 0.8075559735298157,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec49',
                          '_score': 0.8062589764595032,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec7',
                          '_score': 0.8034461140632629,
                          'fields': {'chunk_text': 'The CPI index rose by 6% in '
                                                   'July 2024, raising concerns '
                                                   'about purchasing power.'}},
                         {'_id': 'vec84',
                          '_score': 0.8027160167694092,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec13',
                          '_score': 0.8010239601135254,
                          'fields': {'chunk_text': 'Credit card APRs reached an '
                                                   'all-time high of 22.8% in '
                                                   '2024.'}},
                         {'_id': 'vec53',
                          '_score': 0.8007135391235352,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec60',
                          '_score': 0.7980866432189941,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec91',
                          '_score': 0.7980680465698242,
                          'fields': {'chunk_text': 'The impact of ESG investing on '
                                                   'corporate strategies has been '
                                                   'a major focus in 2024.'}},
                         {'_id': 'vec68',
                          '_score': 0.797269880771637,
                          'fields': {'chunk_text': 'Cybersecurity spending reached '
                                                   'new highs in 2024, reflecting '
                                                   'the growing threat of digital '
                                                   'attacks on infrastructure.'}},
                         {'_id': 'vec59',
                          '_score': 0.795337438583374,
                          'fields': {'chunk_text': 'The adoption of digital '
                                                   'currencies by central banks '
                                                   'increased in 2024, reshaping '
                                                   'monetary policy frameworks.'}},
                         {'_id': 'vec39',
                          '_score': 0.793889045715332,
                          'fields': {'chunk_text': 'The rise in energy prices '
                                                   'significantly impacted '
                                                   'inflation trends during the '
                                                   'first half of 2024.'}},
                         {'_id': 'vec66',
                          '_score': 0.7919396162033081,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec57',
                          '_score': 0.7917722463607788,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec75',
                          '_score': 0.7907494306564331,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec51',
                          '_score': 0.790622889995575,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec89',
                          '_score': 0.7899052500724792,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}}]},
     'usage': {'embed_total_tokens': 12, 'read_units': 1}}
    ```
  </Step>

  <Step title="Search the sparse index">
    Perform a [lexical search](/guides/search/lexical-search).

    For example, the following code searches the sparse index for 40 records that most exactly match the words in the query. Again, because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a sparse vector automatically.

    ```python Python
    sparse_results = sparse_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(sparse_results)
    ```

    ```python Response [expandable]
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 7.0625,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec46',
                          '_score': 7.041015625,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec36',
                          '_score': 6.96875,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 6.9609375,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec49',
                          '_score': 6.65625,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec63',
                          '_score': 6.4765625,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec92',
                          '_score': 5.72265625,
                          'fields': {'chunk_text': 'Income inequality widened in '
                                                   '2024 despite strong economic '
                                                   'growth in developed nations.'}},
                         {'_id': 'vec52',
                          '_score': 5.599609375,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec89',
                          '_score': 4.0078125,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}},
                         {'_id': 'vec62',
                          '_score': 3.99609375,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec57',
                          '_score': 3.93359375,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec69',
                          '_score': 3.8984375,
                          'fields': {'chunk_text': 'The agricultural sector faced '
                                                   'challenges in 2024 due to '
                                                   'extreme weather and rising '
                                                   'input costs.'}},
                         {'_id': 'vec37',
                          '_score': 3.89453125,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec60',
                          '_score': 3.822265625,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec51',
                          '_score': 3.783203125,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec55',
                          '_score': 3.765625,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec70',
                          '_score': 3.76171875,
                          'fields': {'chunk_text': 'Consumer spending patterns '
                                                   'shifted in 2024, with a '
                                                   'greater focus on experiences '
                                                   'over goods.'}},
                         {'_id': 'vec90',
                          '_score': 3.70703125,
                          'fields': {'chunk_text': 'The surge in e-commerce in '
                                                   '2024 was facilitated by '
                                                   'advancements in logistics '
                                                   'technology.'}},
                         {'_id': 'vec87',
                          '_score': 3.69140625,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec78',
                          '_score': 3.673828125,
                          'fields': {'chunk_text': 'Consumer sentiment surveys in '
                                                   '2024 reflected optimism '
                                                   'despite high interest rates.'}},
                         {'_id': 'vec82',
                          '_score': 3.66015625,
                          'fields': {'chunk_text': 'Renewable energy subsidies in '
                                                   '2024 reduced the global '
                                                   'reliance on fossil fuels.'}},
                         {'_id': 'vec53',
                          '_score': 3.642578125,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec94',
                          '_score': 3.625,
                          'fields': {'chunk_text': 'Cyberattacks targeting '
                                                   'financial institutions in 2024 '
                                                   'led to record cybersecurity '
                                                   'spending.'}},
                         {'_id': 'vec45',
                          '_score': 3.607421875,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec47',
                          '_score': 3.576171875,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec84',
                          '_score': 3.5703125,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec41',
                          '_score': 3.5546875,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec65',
                          '_score': 3.537109375,
                          'fields': {'chunk_text': 'The global shipping industry '
                                                   'experienced declining freight '
                                                   'rates in 2024 due to '
                                                   'overcapacity and reduced '
                                                   'demand.'}},
                         {'_id': 'vec96',
                          '_score': 3.53125,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec86',
                          '_score': 3.52734375,
                          'fields': {'chunk_text': 'Digital transformation '
                                                   'initiatives in 2024 drove '
                                                   'productivity gains in the '
                                                   'services sector.'}},
                         {'_id': 'vec95',
                          '_score': 3.5234375,
                          'fields': {'chunk_text': 'Automation in agriculture in '
                                                   '2024 increased yields but '
                                                   'displaced rural workers.'}},
                         {'_id': 'vec64',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec79',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec66',
                          '_score': 3.48046875,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec6',
                          '_score': 3.4765625,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec58',
                          '_score': 3.39453125,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec80',
                          '_score': 3.390625,
                          'fields': {'chunk_text': 'Technological innovation in '
                                                   'the fintech sector disrupted '
                                                   'traditional banking in 2024.'}},
                         {'_id': 'vec75',
                          '_score': 3.37109375,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec67',
                          '_score': 3.357421875,
                          'fields': {'chunk_text': 'Renewable energy projects '
                                                   'accounted for a record share '
                                                   'of global infrastructure '
                                                   'investment in 2024.'}},
                         {'_id': 'vec56',
                          '_score': 3.341796875,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}}]},
     'usage': {'embed_total_tokens': 9, 'read_units': 1}}
    ```
  </Step>

  <Step title="Merge and deduplicate the results">
    Merge the 40 dense and 40 sparse results and deduplicated them based on the field you used to link sparse and dense vectors.

    For example, the following code merges and deduplicates the results based on the `_id` field, resulting in 52 unique results.

    ```python Python
    def merge_chunks(h1, h2):
        """Get the unique hits from two search results and return them as single array of {'_id', 'chunk_text'} dicts, printing each dict on a new line."""
        # Deduplicate by _id
        deduped_hits = {hit['_id']: hit for hit in h1['result']['hits'] + h2['result']['hits']}.values()
        # Sort by _score descending
        sorted_hits = sorted(deduped_hits, key=lambda x: x['_score'], reverse=True)
        # Transform to format for reranking
        result = [{'_id': hit['_id'], 'chunk_text': hit['fields']['chunk_text']} for hit in sorted_hits]
        return result

    merged_results = merge_chunks(sparse_results, dense_results)

    print('[\n   ' + ',\n   '.join(str(obj) for obj in merged_results) + '\n]')
    ```

    ```console Response [expandable]
    [
       {'_id': 'vec92', 'chunk_text': 'Income inequality widened in 2024 despite strong economic growth in developed nations.'},
       {'_id': 'vec69', 'chunk_text': 'The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs.'},
       {'_id': 'vec70', 'chunk_text': 'Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods.'},
       {'_id': 'vec90', 'chunk_text': 'The surge in e-commerce in 2024 was facilitated by advancements in logistics technology.'},
       {'_id': 'vec78', 'chunk_text': 'Consumer sentiment surveys in 2024 reflected optimism despite high interest rates.'},
       {'_id': 'vec82', 'chunk_text': 'Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels.'},
       {'_id': 'vec94', 'chunk_text': 'Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending.'},
       {'_id': 'vec65', 'chunk_text': 'The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand.'},
       {'_id': 'vec86', 'chunk_text': 'Digital transformation initiatives in 2024 drove productivity gains in the services sector.'},
       {'_id': 'vec95', 'chunk_text': 'Automation in agriculture in 2024 increased yields but displaced rural workers.'},
       {'_id': 'vec80', 'chunk_text': 'Technological innovation in the fintech sector disrupted traditional banking in 2024.'},
       {'_id': 'vec67', 'chunk_text': 'Renewable energy projects accounted for a record share of global infrastructure investment in 2024.'},
       {'_id': 'vec35', 'chunk_text': 'Unemployment hit at 2.4% in Q3 of 2024.'},
       {'_id': 'vec36', 'chunk_text': 'Unemployment is expected to hit 2.5% in Q3 of 2024.'},
       {'_id': 'vec6', 'chunk_text': 'Unemployment hit a record low of 3.7% in Q4 of 2024.'},
       {'_id': 'vec42', 'chunk_text': 'Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.'},
       {'_id': 'vec48', 'chunk_text': 'Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.'},
       {'_id': 'vec55', 'chunk_text': 'Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows.'},
       {'_id': 'vec45', 'chunk_text': 'Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations.'},
       {'_id': 'vec72', 'chunk_text': 'In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.'},
       {'_id': 'vec29', 'chunk_text': 'Growth vs. value investing strategies in 2024.'},
       {'_id': 'vec46', 'chunk_text': 'Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.'},
       {'_id': 'vec79', 'chunk_text': 'The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains.'},
       {'_id': 'vec87', 'chunk_text': "The U.S. labor market's resilience in 2024 defied predictions of a severe recession."},
       {'_id': 'vec40', 'chunk_text': 'Labor market trends show a declining participation rate despite record low unemployment in 2024.'},
       {'_id': 'vec37', 'chunk_text': 'In Q3 2025 unemployment for the prior year was revised to 2.2%'},
       {'_id': 'vec58', 'chunk_text': 'Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies.'},
       {'_id': 'vec47', 'chunk_text': 'The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand.'},
       {'_id': 'vec41', 'chunk_text': 'Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand.'},
       {'_id': 'vec56', 'chunk_text': 'Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession.'},
       {'_id': 'vec63', 'chunk_text': 'Population aging emerged as a critical economic issue in 2024, especially in advanced economies.'},
       {'_id': 'vec52', 'chunk_text': 'Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change.'},
       {'_id': 'vec23', 'chunk_text': 'Top SPAC mergers in the technology sector for 2024.'},
       {'_id': 'vec62', 'chunk_text': 'Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities.'},
       {'_id': 'vec64', 'chunk_text': 'Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials.'},
       {'_id': 'vec54', 'chunk_text': 'The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks.'},
       {'_id': 'vec96', 'chunk_text': 'New trade agreements signed 2022 will make an impact in 2024'},
       {'_id': 'vec49', 'chunk_text': "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports."},
       {'_id': 'vec7', 'chunk_text': 'The CPI index rose by 6% in July 2024, raising concerns about purchasing power.'},
       {'_id': 'vec84', 'chunk_text': "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets."},
       {'_id': 'vec13', 'chunk_text': 'Credit card APRs reached an all-time high of 22.8% in 2024.'},
       {'_id': 'vec53', 'chunk_text': 'Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization.'},
       {'_id': 'vec60', 'chunk_text': 'Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness.'},
       {'_id': 'vec91', 'chunk_text': 'The impact of ESG investing on corporate strategies has been a major focus in 2024.'},
       {'_id': 'vec68', 'chunk_text': 'Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure.'},
       {'_id': 'vec59', 'chunk_text': 'The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks.'},
       {'_id': 'vec39', 'chunk_text': 'The rise in energy prices significantly impacted inflation trends during the first half of 2024.'},
       {'_id': 'vec66', 'chunk_text': 'Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship.'},
       {'_id': 'vec57', 'chunk_text': 'Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth.'},
       {'_id': 'vec75', 'chunk_text': 'The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024.'},
       {'_id': 'vec51', 'chunk_text': 'The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth.'},
       {'_id': 'vec89', 'chunk_text': 'Venture capital investments in 2024 leaned heavily toward AI and automation startups.'}
    ]
    ```
  </Step>

  <Step title="Rerank the results">
    Use one of Pinecone's [hosted reranking models](/guides/search/rerank-results#reranking-models) to rerank the merged and deduplicated results based on a unified relevance score and then return a smaller set of the most highly relevant results.

    For example, the following code sends the 52 unique results from the last step to the `bge-reranker-v2-m3` reranking model and returns the top 10 most relevant results.

    ```python Python
    result = pc.inference.rerank(
        model="bge-reranker-v2-m3",
        query=query,
        documents=merged_results,
        rank_fields=["chunk_text"],
        top_n=10,
        return_documents=True,
        parameters={
            "truncate": "END"
        }
    )

    print("Query", query)
    print('-----')
    for row in result.data:
        print(f"{row['document']['_id']} - {round(row['score'], 2)} - {row['document']['chunk_text']}")
    ```

    ```console Response [expandable]
    Query Q3 2024 us economic data
    -----
    vec36 - 0.84 - Unemployment is expected to hit 2.5% in Q3 of 2024.
    vec35 - 0.76 - Unemployment hit at 2.4% in Q3 of 2024.
    vec48 - 0.33 - Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.
    vec37 - 0.25 - In Q3 2025 unemployment for the prior year was revised to 2.2%
    vec42 - 0.21 - Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.
    vec87 - 0.2 - The U.S. labor market's resilience in 2024 defied predictions of a severe recession.
    vec63 - 0.08 - Population aging emerged as a critical economic issue in 2024, especially in advanced economies.
    vec92 - 0.08 - Income inequality widened in 2024 despite strong economic growth in developed nations.
    vec72 - 0.07 - In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.
    vec46 - 0.06 - Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.
    ```
  </Step>
</Steps>

## Use a single hybrid index

You can perform hybrid search with a single hybrid index as follows:

<Steps>
  <Step title="Create a hybrid index">
    To store both dense and sparse vectors in a single index, use the [`create_index`](/reference/api/latest/control-plane/create_index) operation, setting the `vector_type` to `dense` and the `metric` to `dotproduct`. This is the only combination that supports dense/sparse search on a single index.

    ```python Python
    from pinecone.grpc import PineconeGRPC as Pinecone
    from pinecone import ServerlessSpec

    pc = Pinecone(api_key="YOUR_API_KEY")

    index_name = "hybrid-index"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            vector_type="dense",
            dimension=1024,
            metric="dotproduct",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    ```
  </Step>

  <Step title="Generate vectors">
    Use Pinecone's [hosted embedding models](/guides/index-data/create-an-index#embedding-models) to [convert data into dense and sparse vectors](/reference/api/latest/inference/generate-embeddings).

    ```python Python [expandable]
    # Define the records
    data = [
        { "_id": "vec1", "chunk_text": "Apple Inc. issued a $10 billion corporate bond in 2023." },
        { "_id": "vec2", "chunk_text": "ETFs tracking the S&P 500 outperformed active funds last year." },
        { "_id": "vec3", "chunk_text": "Tesla's options volume surged after the latest earnings report." },
        { "_id": "vec4", "chunk_text": "Dividend aristocrats are known for consistently raising payouts." },
        { "_id": "vec5", "chunk_text": "The Federal Reserve raised interest rates by 0.25% to curb inflation." },
        { "_id": "vec6", "chunk_text": "Unemployment hit a record low of 3.7% in Q4 of 2024." },
        { "_id": "vec7", "chunk_text": "The CPI index rose by 6% in July 2024, raising concerns about purchasing power." },
        { "_id": "vec8", "chunk_text": "GDP growth in emerging markets outpaced developed economies." },
        { "_id": "vec9", "chunk_text": "Amazon's acquisition of MGM Studios was valued at $8.45 billion." },
        { "_id": "vec10", "chunk_text": "Alphabet reported a 20% increase in advertising revenue." },
        { "_id": "vec11", "chunk_text": "ExxonMobil announced a special dividend after record profits." },
        { "_id": "vec12", "chunk_text": "Tesla plans a 3-for-1 stock split to attract retail investors." },
        { "_id": "vec13", "chunk_text": "Credit card APRs reached an all-time high of 22.8% in 2024." },
        { "_id": "vec14", "chunk_text": "A 529 college savings plan offers tax advantages for education." },
        { "_id": "vec15", "chunk_text": "Emergency savings should ideally cover 6 months of expenses." },
        { "_id": "vec16", "chunk_text": "The average mortgage rate rose to 7.1% in December." },
        { "_id": "vec17", "chunk_text": "The SEC fined a hedge fund $50 million for insider trading." },
        { "_id": "vec18", "chunk_text": "New ESG regulations require companies to disclose climate risks." },
        { "_id": "vec19", "chunk_text": "The IRS introduced a new tax bracket for high earners." },
        { "_id": "vec20", "chunk_text": "Compliance with GDPR is mandatory for companies operating in Europe." },
        { "_id": "vec21", "chunk_text": "What are the best-performing green bonds in a rising rate environment?" },
        { "_id": "vec22", "chunk_text": "How does inflation impact the real yield of Treasury bonds?" },
        { "_id": "vec23", "chunk_text": "Top SPAC mergers in the technology sector for 2024." },
        { "_id": "vec24", "chunk_text": "Are stablecoins a viable hedge against currency devaluation?" },
        { "_id": "vec25", "chunk_text": "Comparison of Roth IRA vs 401(k) for high-income earners." },
        { "_id": "vec26", "chunk_text": "Stock splits and their effect on investor sentiment." },
        { "_id": "vec27", "chunk_text": "Tech IPOs that disappointed in their first year." },
        { "_id": "vec28", "chunk_text": "Impact of interest rate hikes on bank stocks." },
        { "_id": "vec29", "chunk_text": "Growth vs. value investing strategies in 2024." },
        { "_id": "vec30", "chunk_text": "The role of artificial intelligence in quantitative trading." },
        { "_id": "vec31", "chunk_text": "What are the implications of quantitative tightening on equities?" },
        { "_id": "vec32", "chunk_text": "How does compounding interest affect long-term investments?" },
        { "_id": "vec33", "chunk_text": "What are the best assets to hedge against inflation?" },
        { "_id": "vec34", "chunk_text": "Can ETFs provide better diversification than mutual funds?" },
        { "_id": "vec35", "chunk_text": "Unemployment hit at 2.4% in Q3 of 2024." },
        { "_id": "vec36", "chunk_text": "Unemployment is expected to hit 2.5% in Q3 of 2024." },
        { "_id": "vec37", "chunk_text": "In Q3 2025 unemployment for the prior year was revised to 2.2%"},
        { "_id": "vec38", "chunk_text": "Emerging markets witnessed increased foreign direct investment as global interest rates stabilized." },
        { "_id": "vec39", "chunk_text": "The rise in energy prices significantly impacted inflation trends during the first half of 2024." },
        { "_id": "vec40", "chunk_text": "Labor market trends show a declining participation rate despite record low unemployment in 2024." },
        { "_id": "vec41", "chunk_text": "Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand." },
        { "_id": "vec42", "chunk_text": "Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries." },
        { "_id": "vec43", "chunk_text": "The U.S. dollar weakened against a basket of currencies as the global economy adjusted to shifting trade balances." },
        { "_id": "vec44", "chunk_text": "Central banks worldwide increased gold reserves to hedge against geopolitical and economic instability." },
        { "_id": "vec45", "chunk_text": "Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations." },
        { "_id": "vec46", "chunk_text": "Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects." },
        { "_id": "vec47", "chunk_text": "The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand." },
        { "_id": "vec48", "chunk_text": "Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024." },
        { "_id": "vec49", "chunk_text": "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports." },
        { "_id": "vec50", "chunk_text": "AI-driven automation in the manufacturing sector boosted productivity but raised concerns about job displacement." },
        { "_id": "vec51", "chunk_text": "The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth." },
        { "_id": "vec52", "chunk_text": "Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change." },
        { "_id": "vec53", "chunk_text": "Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization." },
        { "_id": "vec54", "chunk_text": "The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks." },
        { "_id": "vec55", "chunk_text": "Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows." },
        { "_id": "vec56", "chunk_text": "Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession." },
        { "_id": "vec57", "chunk_text": "Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth." },
        { "_id": "vec58", "chunk_text": "Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies." },
        { "_id": "vec59", "chunk_text": "The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks." },
        { "_id": "vec60", "chunk_text": "Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness." },
        { "_id": "vec61", "chunk_text": "The World Bank reported declining poverty rates globally, but regional disparities persisted." },
        { "_id": "vec62", "chunk_text": "Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities." },
        { "_id": "vec63", "chunk_text": "Population aging emerged as a critical economic issue in 2024, especially in advanced economies." },
        { "_id": "vec64", "chunk_text": "Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials." },
        { "_id": "vec65", "chunk_text": "The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand." },
        { "_id": "vec66", "chunk_text": "Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship." },
        { "_id": "vec67", "chunk_text": "Renewable energy projects accounted for a record share of global infrastructure investment in 2024." },
        { "_id": "vec68", "chunk_text": "Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure." },
        { "_id": "vec69", "chunk_text": "The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs." },
        { "_id": "vec70", "chunk_text": "Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods." },
        { "_id": "vec71", "chunk_text": "The economic impact of the 2008 financial crisis was mitigated by quantitative easing policies." },
        { "_id": "vec72", "chunk_text": "In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe." },
        { "_id": "vec73", "chunk_text": "The historical relationship between inflation and unemployment is explained by the Phillips Curve." },
        { "_id": "vec74", "chunk_text": "The World Trade Organization's role in resolving disputes was tested in 2024." },
        { "_id": "vec75", "chunk_text": "The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024." },
        { "_id": "vec76", "chunk_text": "The cost of living crisis has been exacerbated by stagnant wage growth and rising inflation." },
        { "_id": "vec77", "chunk_text": "Supply chain resilience became a top priority for multinational corporations in 2024." },
        { "_id": "vec78", "chunk_text": "Consumer sentiment surveys in 2024 reflected optimism despite high interest rates." },
        { "_id": "vec79", "chunk_text": "The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains." },
        { "_id": "vec80", "chunk_text": "Technological innovation in the fintech sector disrupted traditional banking in 2024." },
        { "_id": "vec81", "chunk_text": "The link between climate change and migration patterns is increasingly recognized." },
        { "_id": "vec82", "chunk_text": "Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels." },
        { "_id": "vec83", "chunk_text": "The economic fallout of geopolitical tensions was evident in rising defense budgets worldwide." },
        { "_id": "vec84", "chunk_text": "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets." },
        { "_id": "vec85", "chunk_text": "Declining birth rates in advanced economies pose long-term challenges for labor markets." },
        { "_id": "vec86", "chunk_text": "Digital transformation initiatives in 2024 drove productivity gains in the services sector." },
        { "_id": "vec87", "chunk_text": "The U.S. labor market's resilience in 2024 defied predictions of a severe recession." },
        { "_id": "vec88", "chunk_text": "New fiscal measures in the European Union aimed to stabilize debt levels post-pandemic." },
        { "_id": "vec89", "chunk_text": "Venture capital investments in 2024 leaned heavily toward AI and automation startups." },
        { "_id": "vec90", "chunk_text": "The surge in e-commerce in 2024 was facilitated by advancements in logistics technology." },
        { "_id": "vec91", "chunk_text": "The impact of ESG investing on corporate strategies has been a major focus in 2024." },
        { "_id": "vec92", "chunk_text": "Income inequality widened in 2024 despite strong economic growth in developed nations." },
        { "_id": "vec93", "chunk_text": "The collapse of FTX highlighted the volatility and risks associated with cryptocurrencies." },
        { "_id": "vec94", "chunk_text": "Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending." },
        { "_id": "vec95", "chunk_text": "Automation in agriculture in 2024 increased yields but displaced rural workers." },
        { "_id": "vec96", "chunk_text": "New trade agreements signed 2022 will make an impact in 2024"},
    ]
    ```

    ```python Python
    # Convert the chunk_text into dense vectors
    dense_embeddings = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[d['chunk_text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )

    # Convert the chunk_text into sparse vectors
    sparse_embeddings = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=[d['chunk_text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )
    ```
  </Step>

  <Step title="Upsert records with dense and sparse vectors">
    Use the [`upsert`](/reference/api/latest/data-plane/upsert) operation, specifying dense values in the `value` parameter and sparse values in the `sparse_values` parameter.

    <Note>
      Only dense indexes using the [dotproduct distance metric](/guides/index-data/indexing-overview#dotproduct) support dense and sparse vectors. Upserting records with dense and sparse vectors into dense indexes with a different distance metric will succeed, but querying will return an error.
    </Note>

    ```Python Python
    # Target the hybrid index
    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    # Each record contains an ID, a dense vector, a sparse vector, and the original text as metadata
    records = []
    for d, de, se in zip(data, dense_embeddings, sparse_embeddings):
        records.append({
            "id": d['_id'],
            "values": de['values'],
            "sparse_values": {'indices': se['sparse_indices'], 'values': se['sparse_values']},
            "metadata": {'text': d['chunk_text']}
        })

    # Upsert the records into the hybrid index
    index.upsert(
        vectors=records,
        namespace="example-namespace"
    )
    ```
  </Step>

  <Step title="Search the hybrid index">
    Use the [`embed`](/reference/api/latest/inference/generate-embeddings) operation to convert your query into a dense vector and a sparse vector, and then use the [`query`](/reference/api/latest/data-plane/query) operation to search the hybrid index for the 40 most relevant records.

    ```Python Python
    query = "Q3 2024 us economic data"

    # Convert the query into a dense vector
    dense_query_embedding = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=query,
        parameters={"input_type": "query", "truncate": "END"}
    )

    # Convert the query into a sparse vector
    sparse_query_embedding = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=query,
        parameters={"input_type": "query", "truncate": "END"}
    )

    for d, s in zip(dense_query_embedding, sparse_query_embedding):
        query_response = index.query(
            namespace="example-namespace",
            top_k=40,
            vector=d['values'],
            sparse_vector={'indices': s['sparse_indices'], 'values': s['sparse_values']},
            include_values=False,
            include_metadata=True
        )
        print(query_response)
    ```

    ```python Response [expandable]
    {'matches': [{'id': 'vec35',
                  'metadata': {'text': 'Unemployment hit at 2.4% in Q3 of 2024.'},
                  'score': 7.92519569,
                  'values': []},
                 {'id': 'vec46',
                  'metadata': {'text': 'Economic recovery in Q2 2024 relied '
                                       'heavily on government spending in '
                                       'infrastructure and green energy projects.'},
                  'score': 7.86733627,
                  'values': []},
                 {'id': 'vec36',
                  'metadata': {'text': 'Unemployment is expected to hit 2.5% in Q3 '
                                       'of 2024.'},
                  'score': 7.82636,
                  'values': []},
                 {'id': 'vec42',
                  'metadata': {'text': 'Tech sector layoffs in Q3 2024 have '
                                       'reshaped hiring trends across high-growth '
                                       'industries.'},
                  'score': 7.79465914,
                  'values': []},
                 {'id': 'vec49',
                  'metadata': {'text': "China's economic growth in 2024 slowed to "
                                       'its lowest level in decades due to '
                                       'structural reforms and weak exports.'},
                  'score': 7.46323156,
                  'values': []},
                 {'id': 'vec63',
                  'metadata': {'text': 'Population aging emerged as a critical '
                                       'economic issue in 2024, especially in '
                                       'advanced economies.'},
                  'score': 7.29055929,
                  'values': []},
                 {'id': 'vec92',
                  'metadata': {'text': 'Income inequality widened in 2024 despite '
                                       'strong economic growth in developed '
                                       'nations.'},
                  'score': 6.51210213,
                  'values': []},
                 {'id': 'vec52',
                  'metadata': {'text': 'Record-breaking weather events in early '
                                       '2024 have highlighted the growing economic '
                                       'impact of climate change.'},
                  'score': 6.4125514,
                  'values': []},
                 {'id': 'vec62',
                  'metadata': {'text': 'Private equity activity in 2024 focused on '
                                       'renewable energy and technology sectors '
                                       'amid shifting investor priorities.'},
                  'score': 4.8084693,
                  'values': []},
                 {'id': 'vec89',
                  'metadata': {'text': 'Venture capital investments in 2024 leaned '
                                       'heavily toward AI and automation '
                                       'startups.'},
                  'score': 4.7974205,
                  'values': []},
                 {'id': 'vec57',
                  'metadata': {'text': 'Startups in 2024 faced tighter funding '
                                       'conditions as venture capitalists focused '
                                       'on profitability over growth.'},
                  'score': 4.72518444,
                  'values': []},
                 {'id': 'vec37',
                  'metadata': {'text': 'In Q3 2025 unemployment for the prior year '
                                       'was revised to 2.2%'},
                  'score': 4.71824408,
                  'values': []},
                 {'id': 'vec69',
                  'metadata': {'text': 'The agricultural sector faced challenges '
                                       'in 2024 due to extreme weather and rising '
                                       'input costs.'},
                  'score': 4.66726208,
                  'values': []},
                 {'id': 'vec60',
                  'metadata': {'text': 'Healthcare spending in 2024 surged as '
                                       'governments expanded access to preventive '
                                       'care and pandemic preparedness.'},
                  'score': 4.62045908,
                  'values': []},
                 {'id': 'vec55',
                  'metadata': {'text': 'Trade tensions between the U.S. and China '
                                       'escalated in 2024, impacting global supply '
                                       'chains and investment flows.'},
                  'score': 4.59764862,
                  'values': []},
                 {'id': 'vec51',
                  'metadata': {'text': 'The European Union introduced new fiscal '
                                       'policies in 2024 aimed at reducing public '
                                       'debt without stifling growth.'},
                  'score': 4.57397079,
                  'values': []},
                 {'id': 'vec70',
                  'metadata': {'text': 'Consumer spending patterns shifted in '
                                       '2024, with a greater focus on experiences '
                                       'over goods.'},
                  'score': 4.55043507,
                  'values': []},
                 {'id': 'vec87',
                  'metadata': {'text': "The U.S. labor market's resilience in 2024 "
                                       'defied predictions of a severe recession.'},
                  'score': 4.51785707,
                  'values': []},
                 {'id': 'vec90',
                  'metadata': {'text': 'The surge in e-commerce in 2024 was '
                                       'facilitated by advancements in logistics '
                                       'technology.'},
                  'score': 4.47754288,
                  'values': []},
                 {'id': 'vec78',
                  'metadata': {'text': 'Consumer sentiment surveys in 2024 '
                                       'reflected optimism despite high interest '
                                       'rates.'},
                  'score': 4.46246624,
                  'values': []},
                 {'id': 'vec53',
                  'metadata': {'text': 'Cryptocurrencies faced regulatory scrutiny '
                                       'in 2024, leading to volatility and reduced '
                                       'market capitalization.'},
                  'score': 4.4435873,
                  'values': []},
                 {'id': 'vec45',
                  'metadata': {'text': 'Corporate earnings in Q4 2024 were largely '
                                       'impacted by rising raw material costs and '
                                       'currency fluctuations.'},
                  'score': 4.43836403,
                  'values': []},
                 {'id': 'vec82',
                  'metadata': {'text': 'Renewable energy subsidies in 2024 reduced '
                                       'the global reliance on fossil fuels.'},
                  'score': 4.43601322,
                  'values': []},
                 {'id': 'vec94',
                  'metadata': {'text': 'Cyberattacks targeting financial '
                                       'institutions in 2024 led to record '
                                       'cybersecurity spending.'},
                  'score': 4.41334057,
                  'values': []},
                 {'id': 'vec47',
                  'metadata': {'text': 'The housing market saw a rebound in late '
                                       '2024, driven by falling mortgage rates and '
                                       'pent-up demand.'},
                  'score': 4.39900732,
                  'values': []},
                 {'id': 'vec41',
                  'metadata': {'text': 'Forecasts of global supply chain '
                                       'disruptions eased in late 2024, but '
                                       'consumer prices remained elevated due to '
                                       'persistent demand.'},
                  'score': 4.37389421,
                  'values': []},
                 {'id': 'vec84',
                  'metadata': {'text': "The IMF's 2024 global outlook highlighted "
                                       'risks of stagflation in emerging markets.'},
                  'score': 4.37335157,
                  'values': []},
                 {'id': 'vec96',
                  'metadata': {'text': 'New trade agreements signed 2022 will make '
                                       'an impact in 2024'},
                  'score': 4.33860636,
                  'values': []},
                 {'id': 'vec79',
                  'metadata': {'text': 'The resurgence of industrial policy in Q1 '
                                       '2024 focused on decoupling critical supply '
                                       'chains.'},
                  'score': 4.33784199,
                  'values': []},
                 {'id': 'vec6',
                  'metadata': {'text': 'Unemployment hit a record low of 3.7% in '
                                       'Q4 of 2024.'},
                  'score': 4.33008051,
                  'values': []},
                 {'id': 'vec65',
                  'metadata': {'text': 'The global shipping industry experienced '
                                       'declining freight rates in 2024 due to '
                                       'overcapacity and reduced demand.'},
                  'score': 4.3228569,
                  'values': []},
                 {'id': 'vec64',
                  'metadata': {'text': 'Rising commodity prices in 2024 strained '
                                       'emerging markets dependent on imports of '
                                       'raw materials.'},
                  'score': 4.32269621,
                  'values': []},
                 {'id': 'vec95',
                  'metadata': {'text': 'Automation in agriculture in 2024 '
                                       'increased yields but displaced rural '
                                       'workers.'},
                  'score': 4.31127262,
                  'values': []},
                 {'id': 'vec86',
                  'metadata': {'text': 'Digital transformation initiatives in 2024 '
                                       'drove productivity gains in the services '
                                       'sector.'},
                  'score': 4.30181122,
                  'values': []},
                 {'id': 'vec66',
                  'metadata': {'text': 'Bank lending to small and medium-sized '
                                       'enterprises surged in 2024 as governments '
                                       'incentivized entrepreneurship.'},
                  'score': 4.27241945,
                  'values': []},
                 {'id': 'vec58',
                  'metadata': {'text': 'Oil production cuts in Q1 2024 by OPEC '
                                       'nations drove prices higher, influencing '
                                       'global energy policies.'},
                  'score': 4.21715498,
                  'values': []},
                 {'id': 'vec80',
                  'metadata': {'text': 'Technological innovation in the fintech '
                                       'sector disrupted traditional banking in '
                                       '2024.'},
                  'score': 4.17712116,
                  'values': []},
                 {'id': 'vec75',
                  'metadata': {'text': 'The collapse of Silicon Valley Bank raised '
                                       'questions about regulatory oversight in '
                                       '2024.'},
                  'score': 4.16192341,
                  'values': []},
                 {'id': 'vec56',
                  'metadata': {'text': 'Consumer confidence indices remained '
                                       'resilient in Q2 2024 despite fears of an '
                                       'impending recession.'},
                  'score': 4.15782213,
                  'values': []},
                 {'id': 'vec67',
                  'metadata': {'text': 'Renewable energy projects accounted for a '
                                       'record share of global infrastructure '
                                       'investment in 2024.'},
                  'score': 4.14623,
                  'values': []}],
     'namespace': 'example-namespace',
     'usage': {'read_units': 9}}
    ```
  </Step>

  <Step title="Search the hybrid index with explicit weighting">
    Because Pinecone views your sparse-dense vector as a single vector, it does not offer a built-in parameter to adjust the weight of a query's dense part against its sparse part; the index is agnostic to density or sparsity of coordinates in your vectors. You may, however, incorporate a linear weighting scheme by customizing your query vector, as we demonstrate in the function below.

    The following example transforms vector values using an alpha parameter.

    ```Python Python
    def hybrid_score_norm(dense, sparse, alpha: float):
        """Hybrid score using a convex combination

        alpha * dense + (1 - alpha) * sparse

        Args:
            dense: Array of floats representing
            sparse: a dict of `indices` and `values`
            alpha: scale between 0 and 1
        """
        if alpha < 0 or alpha > 1:
            raise ValueError("Alpha must be between 0 and 1")
        hs = {
            'indices': sparse['indices'],
            'values':  [v * (1 - alpha) for v in sparse['values']]
        }
        return [v * alpha for v in dense], hs
    ```

    The following example transforms a vector using the above function, then queries a Pinecone index.

    ```Python Python
    sparse_vector = {
       'indices': [10, 45, 16],
       'values':  [0.5, 0.5, 0.2]
    }
    dense_vector = [0.1, 0.2, 0.3]

    hdense, hsparse = hybrid_score_norm(dense_vector, sparse_vector, alpha=0.75)

    query_response = index.query(
        namespace="example-namespace",
        top_k=10,
        vector=hdense,
        sparse_vector=hsparse
    )
    ```
  </Step>
</Steps>

# Hybrid search

[Semantic search](/guides/search/semantic-search) and [lexical search](/guides/search/lexical-search) are powerful information retrieval techniques, but each has notable limitations. For example, semantic search can miss results based on exact keyword matches, especially in scenarios involving domain-specific terminology, while lexical search can miss results based on relationships, such as synonyms and paraphrases.

This page shows you how to lift these limitations by combining semantic and lexical search. This is often called hybrid search.

## Hybrid search approaches

There are two ways to perform hybrid search in Pinecone:

* [Use separate dense and sparse indexes](#use-separate-dense-and-sparse-indexes). This is the **recommended** approach because it provides the most flexibility.
* [Use a single hybrid index](#use-a-single-hybrid-index). This approach is simpler to implement but doesn't support a few useful features.

The following table summarizes the pros and cons between the two approaches:

| Approach                          | Pros                                                                                                                                                                                                                                                                                       | Cons                                                                                                                                                                            |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Separate dense and sparse indexes | <ul><li>You can start with dense for semantic search and add sparse for lexical search later.</li><li>You can do sparse-only queries.</li><li>You can rerank at multiple levels (for each index and for merged results).</li><li>You can use integrated embedding and reranking.</li></ul> | <ul><li>You need to manage and make requests to two separate indexes.</li><li>You need to maintain the linkage between sparse and dense vectors in different indexes.</li></ul> |
| Single hybrid index               | <ul><li>You make requests to only a single index.</li><li>The linkage between dense and sparse vectors is implicit.</li></ul>                                                                                                                                                              | <ul><li>You can't do sparse-only queries.</li><li>You can't use integrated embedding and reranking.</li></ul>                                                                   |

## Use separate dense and sparse indexes

This is the recommended way to perform hybrid search in Pinecone. You create separate dense and sparse indexes, upsert dense vectors into the dense index and sparse vectors into the sparse index, and search each index separately. Then you combine and deduplicate the results, use one of Pinecone's [hosted reranking models](/guides/search/rerank-results#reranking-models) to rerank them based on a unified relevance score, and return the most relevant matches.

<Steps>
  <Step title="Create dense and sparse indexes">
    [Create a dense index](/guides/index-data/create-an-index#create-a-dense-index) and [create a sparse index](/guides/index-data/create-an-index#create-a-sparse-index), either with integrated embedding or for vectors created with external models.

    For example, the following code creates indexes with integrated embedding models.

    ```python Python
    from pinecone import Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    dense_index_name = "dense-for-hybrid-py"
    sparse_index_name = "sparse-for-hybrid-py"

    if not pc.has_index(dense_index_name):
        pc.create_index_for_model(
            name=dense_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"llama-text-embed-v2",
                "field_map":{"text": "chunk_text"}
            }
        )

    if not pc.has_index(sparse_index_name):
        pc.create_index_for_model(
            name=sparse_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"pinecone-sparse-english-v0",
                "field_map":{"text": "chunk_text"}
            }
        )
    ```
  </Step>

  <Step title="Upsert dense and sparse vectors">
    [Upsert dense vectors](/guides/index-data/upsert-data#upsert-dense-vectors) into the dense index and [upsert sparse vectors](/guides/index-data/upsert-data#upsert-sparse-vectors) into the sparse index.

    Make sure to establish a linkage between the dense and sparse vectors so you can merge and deduplicate search results later. For example, the following uses `_id` as the linkage, but you can use any other custom field as well. Because the indexes are integrated with embedding models, you provide the source texts and Pinecone converts them to vectors automatically.

    ```python Python [expandable]
    # Define the records
    records = [
        { "_id": "vec1", "chunk_text": "Apple Inc. issued a $10 billion corporate bond in 2023." },
        { "_id": "vec2", "chunk_text": "ETFs tracking the S&P 500 outperformed active funds last year." },
        { "_id": "vec3", "chunk_text": "Tesla's options volume surged after the latest earnings report." },
        { "_id": "vec4", "chunk_text": "Dividend aristocrats are known for consistently raising payouts." },
        { "_id": "vec5", "chunk_text": "The Federal Reserve raised interest rates by 0.25% to curb inflation." },
        { "_id": "vec6", "chunk_text": "Unemployment hit a record low of 3.7% in Q4 of 2024." },
        { "_id": "vec7", "chunk_text": "The CPI index rose by 6% in July 2024, raising concerns about purchasing power." },
        { "_id": "vec8", "chunk_text": "GDP growth in emerging markets outpaced developed economies." },
        { "_id": "vec9", "chunk_text": "Amazon's acquisition of MGM Studios was valued at $8.45 billion." },
        { "_id": "vec10", "chunk_text": "Alphabet reported a 20% increase in advertising revenue." },
        { "_id": "vec11", "chunk_text": "ExxonMobil announced a special dividend after record profits." },
        { "_id": "vec12", "chunk_text": "Tesla plans a 3-for-1 stock split to attract retail investors." },
        { "_id": "vec13", "chunk_text": "Credit card APRs reached an all-time high of 22.8% in 2024." },
        { "_id": "vec14", "chunk_text": "A 529 college savings plan offers tax advantages for education." },
        { "_id": "vec15", "chunk_text": "Emergency savings should ideally cover 6 months of expenses." },
        { "_id": "vec16", "chunk_text": "The average mortgage rate rose to 7.1% in December." },
        { "_id": "vec17", "chunk_text": "The SEC fined a hedge fund $50 million for insider trading." },
        { "_id": "vec18", "chunk_text": "New ESG regulations require companies to disclose climate risks." },
        { "_id": "vec19", "chunk_text": "The IRS introduced a new tax bracket for high earners." },
        { "_id": "vec20", "chunk_text": "Compliance with GDPR is mandatory for companies operating in Europe." },
        { "_id": "vec21", "chunk_text": "What are the best-performing green bonds in a rising rate environment?" },
        { "_id": "vec22", "chunk_text": "How does inflation impact the real yield of Treasury bonds?" },
        { "_id": "vec23", "chunk_text": "Top SPAC mergers in the technology sector for 2024." },
        { "_id": "vec24", "chunk_text": "Are stablecoins a viable hedge against currency devaluation?" },
        { "_id": "vec25", "chunk_text": "Comparison of Roth IRA vs 401(k) for high-income earners." },
        { "_id": "vec26", "chunk_text": "Stock splits and their effect on investor sentiment." },
        { "_id": "vec27", "chunk_text": "Tech IPOs that disappointed in their first year." },
        { "_id": "vec28", "chunk_text": "Impact of interest rate hikes on bank stocks." },
        { "_id": "vec29", "chunk_text": "Growth vs. value investing strategies in 2024." },
        { "_id": "vec30", "chunk_text": "The role of artificial intelligence in quantitative trading." },
        { "_id": "vec31", "chunk_text": "What are the implications of quantitative tightening on equities?" },
        { "_id": "vec32", "chunk_text": "How does compounding interest affect long-term investments?" },
        { "_id": "vec33", "chunk_text": "What are the best assets to hedge against inflation?" },
        { "_id": "vec34", "chunk_text": "Can ETFs provide better diversification than mutual funds?" },
        { "_id": "vec35", "chunk_text": "Unemployment hit at 2.4% in Q3 of 2024." },
        { "_id": "vec36", "chunk_text": "Unemployment is expected to hit 2.5% in Q3 of 2024." },
        { "_id": "vec37", "chunk_text": "In Q3 2025 unemployment for the prior year was revised to 2.2%"},
        { "_id": "vec38", "chunk_text": "Emerging markets witnessed increased foreign direct investment as global interest rates stabilized." },
        { "_id": "vec39", "chunk_text": "The rise in energy prices significantly impacted inflation trends during the first half of 2024." },
        { "_id": "vec40", "chunk_text": "Labor market trends show a declining participation rate despite record low unemployment in 2024." },
        { "_id": "vec41", "chunk_text": "Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand." },
        { "_id": "vec42", "chunk_text": "Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries." },
        { "_id": "vec43", "chunk_text": "The U.S. dollar weakened against a basket of currencies as the global economy adjusted to shifting trade balances." },
        { "_id": "vec44", "chunk_text": "Central banks worldwide increased gold reserves to hedge against geopolitical and economic instability." },
        { "_id": "vec45", "chunk_text": "Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations." },
        { "_id": "vec46", "chunk_text": "Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects." },
        { "_id": "vec47", "chunk_text": "The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand." },
        { "_id": "vec48", "chunk_text": "Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024." },
        { "_id": "vec49", "chunk_text": "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports." },
        { "_id": "vec50", "chunk_text": "AI-driven automation in the manufacturing sector boosted productivity but raised concerns about job displacement." },
        { "_id": "vec51", "chunk_text": "The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth." },
        { "_id": "vec52", "chunk_text": "Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change." },
        { "_id": "vec53", "chunk_text": "Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization." },
        { "_id": "vec54", "chunk_text": "The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks." },
        { "_id": "vec55", "chunk_text": "Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows." },
        { "_id": "vec56", "chunk_text": "Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession." },
        { "_id": "vec57", "chunk_text": "Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth." },
        { "_id": "vec58", "chunk_text": "Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies." },
        { "_id": "vec59", "chunk_text": "The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks." },
        { "_id": "vec60", "chunk_text": "Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness." },
        { "_id": "vec61", "chunk_text": "The World Bank reported declining poverty rates globally, but regional disparities persisted." },
        { "_id": "vec62", "chunk_text": "Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities." },
        { "_id": "vec63", "chunk_text": "Population aging emerged as a critical economic issue in 2024, especially in advanced economies." },
        { "_id": "vec64", "chunk_text": "Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials." },
        { "_id": "vec65", "chunk_text": "The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand." },
        { "_id": "vec66", "chunk_text": "Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship." },
        { "_id": "vec67", "chunk_text": "Renewable energy projects accounted for a record share of global infrastructure investment in 2024." },
        { "_id": "vec68", "chunk_text": "Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure." },
        { "_id": "vec69", "chunk_text": "The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs." },
        { "_id": "vec70", "chunk_text": "Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods." },
        { "_id": "vec71", "chunk_text": "The economic impact of the 2008 financial crisis was mitigated by quantitative easing policies." },
        { "_id": "vec72", "chunk_text": "In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe." },
        { "_id": "vec73", "chunk_text": "The historical relationship between inflation and unemployment is explained by the Phillips Curve." },
        { "_id": "vec74", "chunk_text": "The World Trade Organization's role in resolving disputes was tested in 2024." },
        { "_id": "vec75", "chunk_text": "The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024." },
        { "_id": "vec76", "chunk_text": "The cost of living crisis has been exacerbated by stagnant wage growth and rising inflation." },
        { "_id": "vec77", "chunk_text": "Supply chain resilience became a top priority for multinational corporations in 2024." },
        { "_id": "vec78", "chunk_text": "Consumer sentiment surveys in 2024 reflected optimism despite high interest rates." },
        { "_id": "vec79", "chunk_text": "The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains." },
        { "_id": "vec80", "chunk_text": "Technological innovation in the fintech sector disrupted traditional banking in 2024." },
        { "_id": "vec81", "chunk_text": "The link between climate change and migration patterns is increasingly recognized." },
        { "_id": "vec82", "chunk_text": "Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels." },
        { "_id": "vec83", "chunk_text": "The economic fallout of geopolitical tensions was evident in rising defense budgets worldwide." },
        { "_id": "vec84", "chunk_text": "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets." },
        { "_id": "vec85", "chunk_text": "Declining birth rates in advanced economies pose long-term challenges for labor markets." },
        { "_id": "vec86", "chunk_text": "Digital transformation initiatives in 2024 drove productivity gains in the services sector." },
        { "_id": "vec87", "chunk_text": "The U.S. labor market's resilience in 2024 defied predictions of a severe recession." },
        { "_id": "vec88", "chunk_text": "New fiscal measures in the European Union aimed to stabilize debt levels post-pandemic." },
        { "_id": "vec89", "chunk_text": "Venture capital investments in 2024 leaned heavily toward AI and automation startups." },
        { "_id": "vec90", "chunk_text": "The surge in e-commerce in 2024 was facilitated by advancements in logistics technology." },
        { "_id": "vec91", "chunk_text": "The impact of ESG investing on corporate strategies has been a major focus in 2024." },
        { "_id": "vec92", "chunk_text": "Income inequality widened in 2024 despite strong economic growth in developed nations." },
        { "_id": "vec93", "chunk_text": "The collapse of FTX highlighted the volatility and risks associated with cryptocurrencies." },
        { "_id": "vec94", "chunk_text": "Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending." },
        { "_id": "vec95", "chunk_text": "Automation in agriculture in 2024 increased yields but displaced rural workers." },
        { "_id": "vec96", "chunk_text": "New trade agreements signed 2022 will make an impact in 2024"},
    ]
    ```

    ```python Python
    # Target the dense and sparse indexes
    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    dense_index = pc.Index(host="INDEX_HOST")
    sparse_index = pc.Index(host="INDEX_HOST")

    # Upsert the records
    # The `chunk_text` fields are converted to dense and sparse vectors
    dense_index.upsert_records("example-namespace", records)
    sparse_index.upsert_records("example-namespace", records)
    ```
  </Step>

  <Step title="Search the dense index">
    Perform a [semantic search](/guides/search/semantic-search) on the dense index.

    For example, the following code searches the dense index for 40 records most semantically related to the query "Q3 2024 us economic data". Because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a dense vector automatically.

    ```python Python
    query = "Q3 2024 us economic data"

    dense_results = dense_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(dense_results)
    ```

    ```python Response [expandable]
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 0.8629686832427979,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec36',
                          '_score': 0.8573639988899231,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec6',
                          '_score': 0.8535352945327759,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 0.8336166739463806,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec48',
                          '_score': 0.8328524827957153,
                          'fields': {'chunk_text': 'Wage growth outpaced inflation '
                                                   'for the first time in years, '
                                                   'signaling improved purchasing '
                                                   'power in 2024.'}},
                         {'_id': 'vec55',
                          '_score': 0.8322604298591614,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec45',
                          '_score': 0.8309446573257446,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec72',
                          '_score': 0.8275909423828125,
                          'fields': {'chunk_text': 'In early 2024, global GDP '
                                                   'growth slowed, driven by '
                                                   'weaker exports in Asia and '
                                                   'Europe.'}},
                         {'_id': 'vec29',
                          '_score': 0.8270887136459351,
                          'fields': {'chunk_text': 'Growth vs. value investing '
                                                   'strategies in 2024.'}},
                         {'_id': 'vec46',
                          '_score': 0.8263787627220154,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec79',
                          '_score': 0.8258304595947266,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec87',
                          '_score': 0.8257324695587158,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec40',
                          '_score': 0.8253997564315796,
                          'fields': {'chunk_text': 'Labor market trends show a '
                                                   'declining participation rate '
                                                   'despite record low '
                                                   'unemployment in 2024.'}},
                         {'_id': 'vec37',
                          '_score': 0.8235862255096436,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec58',
                          '_score': 0.8233317136764526,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec47',
                          '_score': 0.8231339454650879,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec41',
                          '_score': 0.8187897801399231,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec56',
                          '_score': 0.8155254125595093,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}},
                         {'_id': 'vec63',
                          '_score': 0.8136948347091675,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec52',
                          '_score': 0.8129132390022278,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec23',
                          '_score': 0.8126378655433655,
                          'fields': {'chunk_text': 'Top SPAC mergers in the '
                                                   'technology sector for 2024.'}},
                         {'_id': 'vec62',
                          '_score': 0.8116977214813232,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec64',
                          '_score': 0.8109902739524841,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec54',
                          '_score': 0.8092231154441833,
                          'fields': {'chunk_text': 'The global tourism sector '
                                                   'showed signs of recovery in '
                                                   'late 2024 after years of '
                                                   'pandemic-related setbacks.'}},
                         {'_id': 'vec96',
                          '_score': 0.8075559735298157,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec49',
                          '_score': 0.8062589764595032,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec7',
                          '_score': 0.8034461140632629,
                          'fields': {'chunk_text': 'The CPI index rose by 6% in '
                                                   'July 2024, raising concerns '
                                                   'about purchasing power.'}},
                         {'_id': 'vec84',
                          '_score': 0.8027160167694092,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec13',
                          '_score': 0.8010239601135254,
                          'fields': {'chunk_text': 'Credit card APRs reached an '
                                                   'all-time high of 22.8% in '
                                                   '2024.'}},
                         {'_id': 'vec53',
                          '_score': 0.8007135391235352,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec60',
                          '_score': 0.7980866432189941,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec91',
                          '_score': 0.7980680465698242,
                          'fields': {'chunk_text': 'The impact of ESG investing on '
                                                   'corporate strategies has been '
                                                   'a major focus in 2024.'}},
                         {'_id': 'vec68',
                          '_score': 0.797269880771637,
                          'fields': {'chunk_text': 'Cybersecurity spending reached '
                                                   'new highs in 2024, reflecting '
                                                   'the growing threat of digital '
                                                   'attacks on infrastructure.'}},
                         {'_id': 'vec59',
                          '_score': 0.795337438583374,
                          'fields': {'chunk_text': 'The adoption of digital '
                                                   'currencies by central banks '
                                                   'increased in 2024, reshaping '
                                                   'monetary policy frameworks.'}},
                         {'_id': 'vec39',
                          '_score': 0.793889045715332,
                          'fields': {'chunk_text': 'The rise in energy prices '
                                                   'significantly impacted '
                                                   'inflation trends during the '
                                                   'first half of 2024.'}},
                         {'_id': 'vec66',
                          '_score': 0.7919396162033081,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec57',
                          '_score': 0.7917722463607788,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec75',
                          '_score': 0.7907494306564331,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec51',
                          '_score': 0.790622889995575,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec89',
                          '_score': 0.7899052500724792,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}}]},
     'usage': {'embed_total_tokens': 12, 'read_units': 1}}
    ```
  </Step>

  <Step title="Search the sparse index">
    Perform a [lexical search](/guides/search/lexical-search).

    For example, the following code searches the sparse index for 40 records that most exactly match the words in the query. Again, because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a sparse vector automatically.

    ```python Python
    sparse_results = sparse_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(sparse_results)
    ```

    ```python Response [expandable]
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 7.0625,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec46',
                          '_score': 7.041015625,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec36',
                          '_score': 6.96875,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 6.9609375,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec49',
                          '_score': 6.65625,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec63',
                          '_score': 6.4765625,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec92',
                          '_score': 5.72265625,
                          'fields': {'chunk_text': 'Income inequality widened in '
                                                   '2024 despite strong economic '
                                                   'growth in developed nations.'}},
                         {'_id': 'vec52',
                          '_score': 5.599609375,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec89',
                          '_score': 4.0078125,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}},
                         {'_id': 'vec62',
                          '_score': 3.99609375,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec57',
                          '_score': 3.93359375,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec69',
                          '_score': 3.8984375,
                          'fields': {'chunk_text': 'The agricultural sector faced '
                                                   'challenges in 2024 due to '
                                                   'extreme weather and rising '
                                                   'input costs.'}},
                         {'_id': 'vec37',
                          '_score': 3.89453125,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec60',
                          '_score': 3.822265625,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec51',
                          '_score': 3.783203125,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec55',
                          '_score': 3.765625,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec70',
                          '_score': 3.76171875,
                          'fields': {'chunk_text': 'Consumer spending patterns '
                                                   'shifted in 2024, with a '
                                                   'greater focus on experiences '
                                                   'over goods.'}},
                         {'_id': 'vec90',
                          '_score': 3.70703125,
                          'fields': {'chunk_text': 'The surge in e-commerce in '
                                                   '2024 was facilitated by '
                                                   'advancements in logistics '
                                                   'technology.'}},
                         {'_id': 'vec87',
                          '_score': 3.69140625,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec78',
                          '_score': 3.673828125,
                          'fields': {'chunk_text': 'Consumer sentiment surveys in '
                                                   '2024 reflected optimism '
                                                   'despite high interest rates.'}},
                         {'_id': 'vec82',
                          '_score': 3.66015625,
                          'fields': {'chunk_text': 'Renewable energy subsidies in '
                                                   '2024 reduced the global '
                                                   'reliance on fossil fuels.'}},
                         {'_id': 'vec53',
                          '_score': 3.642578125,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec94',
                          '_score': 3.625,
                          'fields': {'chunk_text': 'Cyberattacks targeting '
                                                   'financial institutions in 2024 '
                                                   'led to record cybersecurity '
                                                   'spending.'}},
                         {'_id': 'vec45',
                          '_score': 3.607421875,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec47',
                          '_score': 3.576171875,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec84',
                          '_score': 3.5703125,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec41',
                          '_score': 3.5546875,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec65',
                          '_score': 3.537109375,
                          'fields': {'chunk_text': 'The global shipping industry '
                                                   'experienced declining freight '
                                                   'rates in 2024 due to '
                                                   'overcapacity and reduced '
                                                   'demand.'}},
                         {'_id': 'vec96',
                          '_score': 3.53125,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec86',
                          '_score': 3.52734375,
                          'fields': {'chunk_text': 'Digital transformation '
                                                   'initiatives in 2024 drove '
                                                   'productivity gains in the '
                                                   'services sector.'}},
                         {'_id': 'vec95',
                          '_score': 3.5234375,
                          'fields': {'chunk_text': 'Automation in agriculture in '
                                                   '2024 increased yields but '
                                                   'displaced rural workers.'}},
                         {'_id': 'vec64',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec79',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec66',
                          '_score': 3.48046875,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec6',
                          '_score': 3.4765625,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec58',
                          '_score': 3.39453125,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec80',
                          '_score': 3.390625,
                          'fields': {'chunk_text': 'Technological innovation in '
                                                   'the fintech sector disrupted '
                                                   'traditional banking in 2024.'}},
                         {'_id': 'vec75',
                          '_score': 3.37109375,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec67',
                          '_score': 3.357421875,
                          'fields': {'chunk_text': 'Renewable energy projects '
                                                   'accounted for a record share '
                                                   'of global infrastructure '
                                                   'investment in 2024.'}},
                         {'_id': 'vec56',
                          '_score': 3.341796875,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}}]},
     'usage': {'embed_total_tokens': 9, 'read_units': 1}}
    ```
  </Step>

  <Step title="Merge and deduplicate the results">
    Merge the 40 dense and 40 sparse results and deduplicated them based on the field you used to link sparse and dense vectors.

    For example, the following code merges and deduplicates the results based on the `_id` field, resulting in 52 unique results.

    ```python Python
    def merge_chunks(h1, h2):
        """Get the unique hits from two search results and return them as single array of {'_id', 'chunk_text'} dicts, printing each dict on a new line."""
        # Deduplicate by _id
        deduped_hits = {hit['_id']: hit for hit in h1['result']['hits'] + h2['result']['hits']}.values()
        # Sort by _score descending
        sorted_hits = sorted(deduped_hits, key=lambda x: x['_score'], reverse=True)
        # Transform to format for reranking
        result = [{'_id': hit['_id'], 'chunk_text': hit['fields']['chunk_text']} for hit in sorted_hits]
        return result

    merged_results = merge_chunks(sparse_results, dense_results)

    print('[\n   ' + ',\n   '.join(str(obj) for obj in merged_results) + '\n]')
    ```

    ```console Response [expandable]
    [
       {'_id': 'vec92', 'chunk_text': 'Income inequality widened in 2024 despite strong economic growth in developed nations.'},
       {'_id': 'vec69', 'chunk_text': 'The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs.'},
       {'_id': 'vec70', 'chunk_text': 'Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods.'},
       {'_id': 'vec90', 'chunk_text': 'The surge in e-commerce in 2024 was facilitated by advancements in logistics technology.'},
       {'_id': 'vec78', 'chunk_text': 'Consumer sentiment surveys in 2024 reflected optimism despite high interest rates.'},
       {'_id': 'vec82', 'chunk_text': 'Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels.'},
       {'_id': 'vec94', 'chunk_text': 'Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending.'},
       {'_id': 'vec65', 'chunk_text': 'The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand.'},
       {'_id': 'vec86', 'chunk_text': 'Digital transformation initiatives in 2024 drove productivity gains in the services sector.'},
       {'_id': 'vec95', 'chunk_text': 'Automation in agriculture in 2024 increased yields but displaced rural workers.'},
       {'_id': 'vec80', 'chunk_text': 'Technological innovation in the fintech sector disrupted traditional banking in 2024.'},
       {'_id': 'vec67', 'chunk_text': 'Renewable energy projects accounted for a record share of global infrastructure investment in 2024.'},
       {'_id': 'vec35', 'chunk_text': 'Unemployment hit at 2.4% in Q3 of 2024.'},
       {'_id': 'vec36', 'chunk_text': 'Unemployment is expected to hit 2.5% in Q3 of 2024.'},
       {'_id': 'vec6', 'chunk_text': 'Unemployment hit a record low of 3.7% in Q4 of 2024.'},
       {'_id': 'vec42', 'chunk_text': 'Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.'},
       {'_id': 'vec48', 'chunk_text': 'Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.'},
       {'_id': 'vec55', 'chunk_text': 'Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows.'},
       {'_id': 'vec45', 'chunk_text': 'Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations.'},
       {'_id': 'vec72', 'chunk_text': 'In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.'},
       {'_id': 'vec29', 'chunk_text': 'Growth vs. value investing strategies in 2024.'},
       {'_id': 'vec46', 'chunk_text': 'Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.'},
       {'_id': 'vec79', 'chunk_text': 'The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains.'},
       {'_id': 'vec87', 'chunk_text': "The U.S. labor market's resilience in 2024 defied predictions of a severe recession."},
       {'_id': 'vec40', 'chunk_text': 'Labor market trends show a declining participation rate despite record low unemployment in 2024.'},
       {'_id': 'vec37', 'chunk_text': 'In Q3 2025 unemployment for the prior year was revised to 2.2%'},
       {'_id': 'vec58', 'chunk_text': 'Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies.'},
       {'_id': 'vec47', 'chunk_text': 'The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand.'},
       {'_id': 'vec41', 'chunk_text': 'Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand.'},
       {'_id': 'vec56', 'chunk_text': 'Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession.'},
       {'_id': 'vec63', 'chunk_text': 'Population aging emerged as a critical economic issue in 2024, especially in advanced economies.'},
       {'_id': 'vec52', 'chunk_text': 'Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change.'},
       {'_id': 'vec23', 'chunk_text': 'Top SPAC mergers in the technology sector for 2024.'},
       {'_id': 'vec62', 'chunk_text': 'Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities.'},
       {'_id': 'vec64', 'chunk_text': 'Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials.'},
       {'_id': 'vec54', 'chunk_text': 'The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks.'},
       {'_id': 'vec96', 'chunk_text': 'New trade agreements signed 2022 will make an impact in 2024'},
       {'_id': 'vec49', 'chunk_text': "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports."},
       {'_id': 'vec7', 'chunk_text': 'The CPI index rose by 6% in July 2024, raising concerns about purchasing power.'},
       {'_id': 'vec84', 'chunk_text': "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets."},
       {'_id': 'vec13', 'chunk_text': 'Credit card APRs reached an all-time high of 22.8% in 2024.'},
       {'_id': 'vec53', 'chunk_text': 'Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization.'},
       {'_id': 'vec60', 'chunk_text': 'Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness.'},
       {'_id': 'vec91', 'chunk_text': 'The impact of ESG investing on corporate strategies has been a major focus in 2024.'},
       {'_id': 'vec68', 'chunk_text': 'Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure.'},
       {'_id': 'vec59', 'chunk_text': 'The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks.'},
       {'_id': 'vec39', 'chunk_text': 'The rise in energy prices significantly impacted inflation trends during the first half of 2024.'},
       {'_id': 'vec66', 'chunk_text': 'Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship.'},
       {'_id': 'vec57', 'chunk_text': 'Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth.'},
       {'_id': 'vec75', 'chunk_text': 'The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024.'},
       {'_id': 'vec51', 'chunk_text': 'The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth.'},
       {'_id': 'vec89', 'chunk_text': 'Venture capital investments in 2024 leaned heavily toward AI and automation startups.'}
    ]
    ```
  </Step>

  <Step title="Rerank the results">
    Use one of Pinecone's [hosted reranking models](/guides/search/rerank-results#reranking-models) to rerank the merged and deduplicated results based on a unified relevance score and then return a smaller set of the most highly relevant results.

    For example, the following code sends the 52 unique results from the last step to the `bge-reranker-v2-m3` reranking model and returns the top 10 most relevant results.

    ```python Python
    result = pc.inference.rerank(
        model="bge-reranker-v2-m3",
        query=query,
        documents=merged_results,
        rank_fields=["chunk_text"],
        top_n=10,
        return_documents=True,
        parameters={
            "truncate": "END"
        }
    )

    print("Query", query)
    print('-----')
    for row in result.data:
        print(f"{row['document']['_id']} - {round(row['score'], 2)} - {row['document']['chunk_text']}")
    ```

    ```console Response [expandable]
    Query Q3 2024 us economic data
    -----
    vec36 - 0.84 - Unemployment is expected to hit 2.5% in Q3 of 2024.
    vec35 - 0.76 - Unemployment hit at 2.4% in Q3 of 2024.
    vec48 - 0.33 - Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.
    vec37 - 0.25 - In Q3 2025 unemployment for the prior year was revised to 2.2%
    vec42 - 0.21 - Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.
    vec87 - 0.2 - The U.S. labor market's resilience in 2024 defied predictions of a severe recession.
    vec63 - 0.08 - Population aging emerged as a critical economic issue in 2024, especially in advanced economies.
    vec92 - 0.08 - Income inequality widened in 2024 despite strong economic growth in developed nations.
    vec72 - 0.07 - In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.
    vec46 - 0.06 - Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.
    ```
  </Step>
</Steps>

## Use a single hybrid index

You can perform hybrid search with a single hybrid index as follows:

<Steps>
  <Step title="Create a hybrid index">
    To store both dense and sparse vectors in a single index, use the [`create_index`](/reference/api/latest/control-plane/create_index) operation, setting the `vector_type` to `dense` and the `metric` to `dotproduct`. This is the only combination that supports dense/sparse search on a single index.

    ```python Python
    from pinecone.grpc import PineconeGRPC as Pinecone
    from pinecone import ServerlessSpec

    pc = Pinecone(api_key="YOUR_API_KEY")

    index_name = "hybrid-index"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            vector_type="dense",
            dimension=1024,
            metric="dotproduct",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    ```
  </Step>

  <Step title="Generate vectors">
    Use Pinecone's [hosted embedding models](/guides/index-data/create-an-index#embedding-models) to [convert data into dense and sparse vectors](/reference/api/latest/inference/generate-embeddings).

    ```python Python [expandable]
    # Define the records
    data = [
        { "_id": "vec1", "chunk_text": "Apple Inc. issued a $10 billion corporate bond in 2023." },
        { "_id": "vec2", "chunk_text": "ETFs tracking the S&P 500 outperformed active funds last year." },
        { "_id": "vec3", "chunk_text": "Tesla's options volume surged after the latest earnings report." },
        { "_id": "vec4", "chunk_text": "Dividend aristocrats are known for consistently raising payouts." },
        { "_id": "vec5", "chunk_text": "The Federal Reserve raised interest rates by 0.25% to curb inflation." },
        { "_id": "vec6", "chunk_text": "Unemployment hit a record low of 3.7% in Q4 of 2024." },
        { "_id": "vec7", "chunk_text": "The CPI index rose by 6% in July 2024, raising concerns about purchasing power." },
        { "_id": "vec8", "chunk_text": "GDP growth in emerging markets outpaced developed economies." },
        { "_id": "vec9", "chunk_text": "Amazon's acquisition of MGM Studios was valued at $8.45 billion." },
        { "_id": "vec10", "chunk_text": "Alphabet reported a 20% increase in advertising revenue." },
        { "_id": "vec11", "chunk_text": "ExxonMobil announced a special dividend after record profits." },
        { "_id": "vec12", "chunk_text": "Tesla plans a 3-for-1 stock split to attract retail investors." },
        { "_id": "vec13", "chunk_text": "Credit card APRs reached an all-time high of 22.8% in 2024." },
        { "_id": "vec14", "chunk_text": "A 529 college savings plan offers tax advantages for education." },
        { "_id": "vec15", "chunk_text": "Emergency savings should ideally cover 6 months of expenses." },
        { "_id": "vec16", "chunk_text": "The average mortgage rate rose to 7.1% in December." },
        { "_id": "vec17", "chunk_text": "The SEC fined a hedge fund $50 million for insider trading." },
        { "_id": "vec18", "chunk_text": "New ESG regulations require companies to disclose climate risks." },
        { "_id": "vec19", "chunk_text": "The IRS introduced a new tax bracket for high earners." },
        { "_id": "vec20", "chunk_text": "Compliance with GDPR is mandatory for companies operating in Europe." },
        { "_id": "vec21", "chunk_text": "What are the best-performing green bonds in a rising rate environment?" },
        { "_id": "vec22", "chunk_text": "How does inflation impact the real yield of Treasury bonds?" },
        { "_id": "vec23", "chunk_text": "Top SPAC mergers in the technology sector for 2024." },
        { "_id": "vec24", "chunk_text": "Are stablecoins a viable hedge against currency devaluation?" },
        { "_id": "vec25", "chunk_text": "Comparison of Roth IRA vs 401(k) for high-income earners." },
        { "_id": "vec26", "chunk_text": "Stock splits and their effect on investor sentiment." },
        { "_id": "vec27", "chunk_text": "Tech IPOs that disappointed in their first year." },
        { "_id": "vec28", "chunk_text": "Impact of interest rate hikes on bank stocks." },
        { "_id": "vec29", "chunk_text": "Growth vs. value investing strategies in 2024." },
        { "_id": "vec30", "chunk_text": "The role of artificial intelligence in quantitative trading." },
        { "_id": "vec31", "chunk_text": "What are the implications of quantitative tightening on equities?" },
        { "_id": "vec32", "chunk_text": "How does compounding interest affect long-term investments?" },
        { "_id": "vec33", "chunk_text": "What are the best assets to hedge against inflation?" },
        { "_id": "vec34", "chunk_text": "Can ETFs provide better diversification than mutual funds?" },
        { "_id": "vec35", "chunk_text": "Unemployment hit at 2.4% in Q3 of 2024." },
        { "_id": "vec36", "chunk_text": "Unemployment is expected to hit 2.5% in Q3 of 2024." },
        { "_id": "vec37", "chunk_text": "In Q3 2025 unemployment for the prior year was revised to 2.2%"},
        { "_id": "vec38", "chunk_text": "Emerging markets witnessed increased foreign direct investment as global interest rates stabilized." },
        { "_id": "vec39", "chunk_text": "The rise in energy prices significantly impacted inflation trends during the first half of 2024." },
        { "_id": "vec40", "chunk_text": "Labor market trends show a declining participation rate despite record low unemployment in 2024." },
        { "_id": "vec41", "chunk_text": "Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand." },
        { "_id": "vec42", "chunk_text": "Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries." },
        { "_id": "vec43", "chunk_text": "The U.S. dollar weakened against a basket of currencies as the global economy adjusted to shifting trade balances." },
        { "_id": "vec44", "chunk_text": "Central banks worldwide increased gold reserves to hedge against geopolitical and economic instability." },
        { "_id": "vec45", "chunk_text": "Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations." },
        { "_id": "vec46", "chunk_text": "Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects." },
        { "_id": "vec47", "chunk_text": "The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand." },
        { "_id": "vec48", "chunk_text": "Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024." },
        { "_id": "vec49", "chunk_text": "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports." },
        { "_id": "vec50", "chunk_text": "AI-driven automation in the manufacturing sector boosted productivity but raised concerns about job displacement." },
        { "_id": "vec51", "chunk_text": "The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth." },
        { "_id": "vec52", "chunk_text": "Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change." },
        { "_id": "vec53", "chunk_text": "Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization." },
        { "_id": "vec54", "chunk_text": "The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks." },
        { "_id": "vec55", "chunk_text": "Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows." },
        { "_id": "vec56", "chunk_text": "Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession." },
        { "_id": "vec57", "chunk_text": "Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth." },
        { "_id": "vec58", "chunk_text": "Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies." },
        { "_id": "vec59", "chunk_text": "The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks." },
        { "_id": "vec60", "chunk_text": "Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness." },
        { "_id": "vec61", "chunk_text": "The World Bank reported declining poverty rates globally, but regional disparities persisted." },
        { "_id": "vec62", "chunk_text": "Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities." },
        { "_id": "vec63", "chunk_text": "Population aging emerged as a critical economic issue in 2024, especially in advanced economies." },
        { "_id": "vec64", "chunk_text": "Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials." },
        { "_id": "vec65", "chunk_text": "The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand." },
        { "_id": "vec66", "chunk_text": "Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship." },
        { "_id": "vec67", "chunk_text": "Renewable energy projects accounted for a record share of global infrastructure investment in 2024." },
        { "_id": "vec68", "chunk_text": "Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure." },
        { "_id": "vec69", "chunk_text": "The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs." },
        { "_id": "vec70", "chunk_text": "Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods." },
        { "_id": "vec71", "chunk_text": "The economic impact of the 2008 financial crisis was mitigated by quantitative easing policies." },
        { "_id": "vec72", "chunk_text": "In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe." },
        { "_id": "vec73", "chunk_text": "The historical relationship between inflation and unemployment is explained by the Phillips Curve." },
        { "_id": "vec74", "chunk_text": "The World Trade Organization's role in resolving disputes was tested in 2024." },
        { "_id": "vec75", "chunk_text": "The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024." },
        { "_id": "vec76", "chunk_text": "The cost of living crisis has been exacerbated by stagnant wage growth and rising inflation." },
        { "_id": "vec77", "chunk_text": "Supply chain resilience became a top priority for multinational corporations in 2024." },
        { "_id": "vec78", "chunk_text": "Consumer sentiment surveys in 2024 reflected optimism despite high interest rates." },
        { "_id": "vec79", "chunk_text": "The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains." },
        { "_id": "vec80", "chunk_text": "Technological innovation in the fintech sector disrupted traditional banking in 2024." },
        { "_id": "vec81", "chunk_text": "The link between climate change and migration patterns is increasingly recognized." },
        { "_id": "vec82", "chunk_text": "Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels." },
        { "_id": "vec83", "chunk_text": "The economic fallout of geopolitical tensions was evident in rising defense budgets worldwide." },
        { "_id": "vec84", "chunk_text": "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets." },
        { "_id": "vec85", "chunk_text": "Declining birth rates in advanced economies pose long-term challenges for labor markets." },
        { "_id": "vec86", "chunk_text": "Digital transformation initiatives in 2024 drove productivity gains in the services sector." },
        { "_id": "vec87", "chunk_text": "The U.S. labor market's resilience in 2024 defied predictions of a severe recession." },
        { "_id": "vec88", "chunk_text": "New fiscal measures in the European Union aimed to stabilize debt levels post-pandemic." },
        { "_id": "vec89", "chunk_text": "Venture capital investments in 2024 leaned heavily toward AI and automation startups." },
        { "_id": "vec90", "chunk_text": "The surge in e-commerce in 2024 was facilitated by advancements in logistics technology." },
        { "_id": "vec91", "chunk_text": "The impact of ESG investing on corporate strategies has been a major focus in 2024." },
        { "_id": "vec92", "chunk_text": "Income inequality widened in 2024 despite strong economic growth in developed nations." },
        { "_id": "vec93", "chunk_text": "The collapse of FTX highlighted the volatility and risks associated with cryptocurrencies." },
        { "_id": "vec94", "chunk_text": "Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending." },
        { "_id": "vec95", "chunk_text": "Automation in agriculture in 2024 increased yields but displaced rural workers." },
        { "_id": "vec96", "chunk_text": "New trade agreements signed 2022 will make an impact in 2024"},
    ]
    ```

    ```python Python
    # Convert the chunk_text into dense vectors
    dense_embeddings = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[d['chunk_text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )

    # Convert the chunk_text into sparse vectors
    sparse_embeddings = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=[d['chunk_text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )
    ```
  </Step>

  <Step title="Upsert records with dense and sparse vectors">
    Use the [`upsert`](/reference/api/latest/data-plane/upsert) operation, specifying dense values in the `value` parameter and sparse values in the `sparse_values` parameter.

    <Note>
      Only dense indexes using the [dotproduct distance metric](/guides/index-data/indexing-overview#dotproduct) support dense and sparse vectors. Upserting records with dense and sparse vectors into dense indexes with a different distance metric will succeed, but querying will return an error.
    </Note>

    ```Python Python
    # Target the hybrid index
    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    # Each record contains an ID, a dense vector, a sparse vector, and the original text as metadata
    records = []
    for d, de, se in zip(data, dense_embeddings, sparse_embeddings):
        records.append({
            "id": d['_id'],
            "values": de['values'],
            "sparse_values": {'indices': se['sparse_indices'], 'values': se['sparse_values']},
            "metadata": {'text': d['chunk_text']}
        })

    # Upsert the records into the hybrid index
    index.upsert(
        vectors=records,
        namespace="example-namespace"
    )
    ```
  </Step>

  <Step title="Search the hybrid index">
    Use the [`embed`](/reference/api/latest/inference/generate-embeddings) operation to convert your query into a dense vector and a sparse vector, and then use the [`query`](/reference/api/latest/data-plane/query) operation to search the hybrid index for the 40 most relevant records.

    ```Python Python
    query = "Q3 2024 us economic data"

    # Convert the query into a dense vector
    dense_query_embedding = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=query,
        parameters={"input_type": "query", "truncate": "END"}
    )

    # Convert the query into a sparse vector
    sparse_query_embedding = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=query,
        parameters={"input_type": "query", "truncate": "END"}
    )

    for d, s in zip(dense_query_embedding, sparse_query_embedding):
        query_response = index.query(
            namespace="example-namespace",
            top_k=40,
            vector=d['values'],
            sparse_vector={'indices': s['sparse_indices'], 'values': s['sparse_values']},
            include_values=False,
            include_metadata=True
        )
        print(query_response)
    ```

    ```python Response [expandable]
    {'matches': [{'id': 'vec35',
                  'metadata': {'text': 'Unemployment hit at 2.4% in Q3 of 2024.'},
                  'score': 7.92519569,
                  'values': []},
                 {'id': 'vec46',
                  'metadata': {'text': 'Economic recovery in Q2 2024 relied '
                                       'heavily on government spending in '
                                       'infrastructure and green energy projects.'},
                  'score': 7.86733627,
                  'values': []},
                 {'id': 'vec36',
                  'metadata': {'text': 'Unemployment is expected to hit 2.5% in Q3 '
                                       'of 2024.'},
                  'score': 7.82636,
                  'values': []},
                 {'id': 'vec42',
                  'metadata': {'text': 'Tech sector layoffs in Q3 2024 have '
                                       'reshaped hiring trends across high-growth '
                                       'industries.'},
                  'score': 7.79465914,
                  'values': []},
                 {'id': 'vec49',
                  'metadata': {'text': "China's economic growth in 2024 slowed to "
                                       'its lowest level in decades due to '
                                       'structural reforms and weak exports.'},
                  'score': 7.46323156,
                  'values': []},
                 {'id': 'vec63',
                  'metadata': {'text': 'Population aging emerged as a critical '
                                       'economic issue in 2024, especially in '
                                       'advanced economies.'},
                  'score': 7.29055929,
                  'values': []},
                 {'id': 'vec92',
                  'metadata': {'text': 'Income inequality widened in 2024 despite '
                                       'strong economic growth in developed '
                                       'nations.'},
                  'score': 6.51210213,
                  'values': []},
                 {'id': 'vec52',
                  'metadata': {'text': 'Record-breaking weather events in early '
                                       '2024 have highlighted the growing economic '
                                       'impact of climate change.'},
                  'score': 6.4125514,
                  'values': []},
                 {'id': 'vec62',
                  'metadata': {'text': 'Private equity activity in 2024 focused on '
                                       'renewable energy and technology sectors '
                                       'amid shifting investor priorities.'},
                  'score': 4.8084693,
                  'values': []},
                 {'id': 'vec89',
                  'metadata': {'text': 'Venture capital investments in 2024 leaned '
                                       'heavily toward AI and automation '
                                       'startups.'},
                  'score': 4.7974205,
                  'values': []},
                 {'id': 'vec57',
                  'metadata': {'text': 'Startups in 2024 faced tighter funding '
                                       'conditions as venture capitalists focused '
                                       'on profitability over growth.'},
                  'score': 4.72518444,
                  'values': []},
                 {'id': 'vec37',
                  'metadata': {'text': 'In Q3 2025 unemployment for the prior year '
                                       'was revised to 2.2%'},
                  'score': 4.71824408,
                  'values': []},
                 {'id': 'vec69',
                  'metadata': {'text': 'The agricultural sector faced challenges '
                                       'in 2024 due to extreme weather and rising '
                                       'input costs.'},
                  'score': 4.66726208,
                  'values': []},
                 {'id': 'vec60',
                  'metadata': {'text': 'Healthcare spending in 2024 surged as '
                                       'governments expanded access to preventive '
                                       'care and pandemic preparedness.'},
                  'score': 4.62045908,
                  'values': []},
                 {'id': 'vec55',
                  'metadata': {'text': 'Trade tensions between the U.S. and China '
                                       'escalated in 2024, impacting global supply '
                                       'chains and investment flows.'},
                  'score': 4.59764862,
                  'values': []},
                 {'id': 'vec51',
                  'metadata': {'text': 'The European Union introduced new fiscal '
                                       'policies in 2024 aimed at reducing public '
                                       'debt without stifling growth.'},
                  'score': 4.57397079,
                  'values': []},
                 {'id': 'vec70',
                  'metadata': {'text': 'Consumer spending patterns shifted in '
                                       '2024, with a greater focus on experiences '
                                       'over goods.'},
                  'score': 4.55043507,
                  'values': []},
                 {'id': 'vec87',
                  'metadata': {'text': "The U.S. labor market's resilience in 2024 "
                                       'defied predictions of a severe recession.'},
                  'score': 4.51785707,
                  'values': []},
                 {'id': 'vec90',
                  'metadata': {'text': 'The surge in e-commerce in 2024 was '
                                       'facilitated by advancements in logistics '
                                       'technology.'},
                  'score': 4.47754288,
                  'values': []},
                 {'id': 'vec78',
                  'metadata': {'text': 'Consumer sentiment surveys in 2024 '
                                       'reflected optimism despite high interest '
                                       'rates.'},
                  'score': 4.46246624,
                  'values': []},
                 {'id': 'vec53',
                  'metadata': {'text': 'Cryptocurrencies faced regulatory scrutiny '
                                       'in 2024, leading to volatility and reduced '
                                       'market capitalization.'},
                  'score': 4.4435873,
                  'values': []},
                 {'id': 'vec45',
                  'metadata': {'text': 'Corporate earnings in Q4 2024 were largely '
                                       'impacted by rising raw material costs and '
                                       'currency fluctuations.'},
                  'score': 4.43836403,
                  'values': []},
                 {'id': 'vec82',
                  'metadata': {'text': 'Renewable energy subsidies in 2024 reduced '
                                       'the global reliance on fossil fuels.'},
                  'score': 4.43601322,
                  'values': []},
                 {'id': 'vec94',
                  'metadata': {'text': 'Cyberattacks targeting financial '
                                       'institutions in 2024 led to record '
                                       'cybersecurity spending.'},
                  'score': 4.41334057,
                  'values': []},
                 {'id': 'vec47',
                  'metadata': {'text': 'The housing market saw a rebound in late '
                                       '2024, driven by falling mortgage rates and '
                                       'pent-up demand.'},
                  'score': 4.39900732,
                  'values': []},
                 {'id': 'vec41',
                  'metadata': {'text': 'Forecasts of global supply chain '
                                       'disruptions eased in late 2024, but '
                                       'consumer prices remained elevated due to '
                                       'persistent demand.'},
                  'score': 4.37389421,
                  'values': []},
                 {'id': 'vec84',
                  'metadata': {'text': "The IMF's 2024 global outlook highlighted "
                                       'risks of stagflation in emerging markets.'},
                  'score': 4.37335157,
                  'values': []},
                 {'id': 'vec96',
                  'metadata': {'text': 'New trade agreements signed 2022 will make '
                                       'an impact in 2024'},
                  'score': 4.33860636,
                  'values': []},
                 {'id': 'vec79',
                  'metadata': {'text': 'The resurgence of industrial policy in Q1 '
                                       '2024 focused on decoupling critical supply '
                                       'chains.'},
                  'score': 4.33784199,
                  'values': []},
                 {'id': 'vec6',
                  'metadata': {'text': 'Unemployment hit a record low of 3.7% in '
                                       'Q4 of 2024.'},
                  'score': 4.33008051,
                  'values': []},
                 {'id': 'vec65',
                  'metadata': {'text': 'The global shipping industry experienced '
                                       'declining freight rates in 2024 due to '
                                       'overcapacity and reduced demand.'},
                  'score': 4.3228569,
                  'values': []},
                 {'id': 'vec64',
                  'metadata': {'text': 'Rising commodity prices in 2024 strained '
                                       'emerging markets dependent on imports of '
                                       'raw materials.'},
                  'score': 4.32269621,
                  'values': []},
                 {'id': 'vec95',
                  'metadata': {'text': 'Automation in agriculture in 2024 '
                                       'increased yields but displaced rural '
                                       'workers.'},
                  'score': 4.31127262,
                  'values': []},
                 {'id': 'vec86',
                  'metadata': {'text': 'Digital transformation initiatives in 2024 '
                                       'drove productivity gains in the services '
                                       'sector.'},
                  'score': 4.30181122,
                  'values': []},
                 {'id': 'vec66',
                  'metadata': {'text': 'Bank lending to small and medium-sized '
                                       'enterprises surged in 2024 as governments '
                                       'incentivized entrepreneurship.'},
                  'score': 4.27241945,
                  'values': []},
                 {'id': 'vec58',
                  'metadata': {'text': 'Oil production cuts in Q1 2024 by OPEC '
                                       'nations drove prices higher, influencing '
                                       'global energy policies.'},
                  'score': 4.21715498,
                  'values': []},
                 {'id': 'vec80',
                  'metadata': {'text': 'Technological innovation in the fintech '
                                       'sector disrupted traditional banking in '
                                       '2024.'},
                  'score': 4.17712116,
                  'values': []},
                 {'id': 'vec75',
                  'metadata': {'text': 'The collapse of Silicon Valley Bank raised '
                                       'questions about regulatory oversight in '
                                       '2024.'},
                  'score': 4.16192341,
                  'values': []},
                 {'id': 'vec56',
                  'metadata': {'text': 'Consumer confidence indices remained '
                                       'resilient in Q2 2024 despite fears of an '
                                       'impending recession.'},
                  'score': 4.15782213,
                  'values': []},
                 {'id': 'vec67',
                  'metadata': {'text': 'Renewable energy projects accounted for a '
                                       'record share of global infrastructure '
                                       'investment in 2024.'},
                  'score': 4.14623,
                  'values': []}],
     'namespace': 'example-namespace',
     'usage': {'read_units': 9}}
    ```
  </Step>

  <Step title="Search the hybrid index with explicit weighting">
    Because Pinecone views your sparse-dense vector as a single vector, it does not offer a built-in parameter to adjust the weight of a query's dense part against its sparse part; the index is agnostic to density or sparsity of coordinates in your vectors. You may, however, incorporate a linear weighting scheme by customizing your query vector, as we demonstrate in the function below.

    The following example transforms vector values using an alpha parameter.

    ```Python Python
    def hybrid_score_norm(dense, sparse, alpha: float):
        """Hybrid score using a convex combination

        alpha * dense + (1 - alpha) * sparse

        Args:
            dense: Array of floats representing
            sparse: a dict of `indices` and `values`
            alpha: scale between 0 and 1
        """
        if alpha < 0 or alpha > 1:
            raise ValueError("Alpha must be between 0 and 1")
        hs = {
            'indices': sparse['indices'],
            'values':  [v * (1 - alpha) for v in sparse['values']]
        }
        return [v * alpha for v in dense], hs
    ```

    The following example transforms a vector using the above function, then queries a Pinecone index.

    ```Python Python
    sparse_vector = {
       'indices': [10, 45, 16],
       'values':  [0.5, 0.5, 0.2]
    }
    dense_vector = [0.1, 0.2, 0.3]

    hdense, hsparse = hybrid_score_norm(dense_vector, sparse_vector, alpha=0.75)

    query_response = index.query(
        namespace="example-namespace",
        top_k=10,
        vector=hdense,
        sparse_vector=hsparse
    )
    ```
  </Step>
</Steps>

# Rerank results

Reranking is used as part of a two-stage vector retrieval process to improve the quality of results. You first query an index for a given number of relevant results, and then you send the query and results to a reranking model. The reranking model scores the results based on their semantic relevance to the query and returns a new, more accurate ranking. This approach is one of the simplest methods for improving quality in retrieval augmented generation (RAG) pipelines.

Pinecone provides [hosted reranking models](#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model or external model to rerank results as a standalone operation.

{/* <Note>
  To run through this guide in your browser, see the [Rerank example notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-reranker.ipynb).
  </Note> */}

## Integrated reranking

To rerank initial results as an integrated part of a query, without any extra steps, use the [`search`](/reference/api/latest/data-plane/search_records) operation with the `rerank` parameter, including the [hosted reranking model](#reranking-models) you want to use, the number of reranked results to return, and the fields to use for reranking, if different than the main query.

For example, the following code searches for the 3 records most semantically related to a query text and uses the `hosted bge-reranker-v2-m3` model to rerank the results and return only the 2 most relevant documents:

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  ranked_results = index.search(
      namespace="example-namespace", 
      query={
          "inputs": {"text": "Disease prevention"}, 
          "top_k": 4
      },
      rerank={
          "model": "bge-reranker-v2-m3",
          "top_n": 2,
          "rank_fields": ["chunk_text"]
      },
      fields=["category", "chunk_text"]
  )

  print(ranked_results)
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

  const response = await namespace.searchRecords({
    query: {
      topK: 2,
      inputs: { text: 'Disease prevention' },
    },
    fields: ['chunk_text', 'category'],
    rerank: {
      model: 'bge-reranker-v2-m3',
      rankFields: ['chunk_text'],
      topN: 2,
    },
  });

  console.log(response);
  ```

  ```java Java
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.SearchRecordsRequestRerank;
  import org.openapitools.db_data.client.model.SearchRecordsResponse;

  import java.util.*;

  public class SearchText {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "integrated-dense-java");

          String query = "Disease prevention";
          List<String> fields = new ArrayList<>();
          fields.add("category");
          fields.add("chunk_text");

          List<String>rankFields = new ArrayList<>();
          rankFields.add("chunk_text");
          SearchRecordsRequestRerank rerank = new SearchRecordsRequestRerank()
                  .query(query)
                  .model("bge-reranker-v2-m3")
                  .topN(2)
                  .rankFields(rankFields);

          SearchRecordsResponse recordsResponseReranked = index.searchRecordsByText(query,  "example-namespace", fields,4, null, rerank);

          System.out.println(recordsResponseReranked);
      }
  }
  ```

  ```go Go
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      } 

      topN := int32(2)
      res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
          Query: pinecone.SearchRecordsQuery{
              TopK: 3,
              Inputs: &map[string]interface{}{
                  "text": "Disease prevention",
              },
          },
          Rerank: &pinecone.SearchRecordsRerank{
              Model:      "bge-reranker-v2-m3",
              TopN:       &topN,
              RankFields: []string{"chunk_text"},
          },
          Fields: &[]string{"chunk_text", "category"},
      })
      if err != nil {
          log.Fatalf("Failed to search records: %v", err)
      }
      fmt.Printf(prettifyStruct(res))
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var response = await index.SearchRecordsAsync(
      "example-namespace",
      new SearchRecordsRequest
      {
          Query = new SearchRecordsRequestQuery
          {
              TopK = 4,
              Inputs = new Dictionary<string, object?> { { "text", "Disease prevention" } },
          },
          Fields = ["category", "chunk_text"],
          Rerank = new SearchRecordsRequestRerank
          {
              Model = "bge-reranker-v2-m3",
              TopN = 2,
              RankFields = ["chunk_text"],
          }
      }
  );

  Console.WriteLine(response);
  ```

  ```shell curl
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: unstable" \
    -d '{
          "query": {
              "inputs": {"text": "Disease prevention"},
              "top_k": 4
          },
          "rerank": {
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          },
          "fields": ["category", "chunk_text"]
       }'
  ```
</CodeGroup>

The response looks as follows. For each hit, the `_score` represents the relevance of a document to the query, normalized between 0 and 1, with scores closer to 1 indicating higher relevance.

<CodeGroup>
  ```python Python
  {'result': {'hits': [{'_id': 'rec3',
                        '_score': 0.004399413242936134,
                        'fields': {'category': 'immune system',
                                   'chunk_text': 'Rich in vitamin C and other '
                                                  'antioxidants, apples '
                                                  'contribute to immune health '
                                                  'and may reduce the risk of '
                                                  'chronic diseases.'}},
                       {'_id': 'rec4',
                        '_score': 0.0029235430993139744,
                        'fields': {'category': 'endocrine system',
                                   'chunk_text': 'The high fiber content in '
                                                  'apples can also help regulate '
                                                  'blood sugar levels, making '
                                                  'them a favorable snack for '
                                                  'people with diabetes.'}}]},
   'usage': {'embed_total_tokens': 8, 'read_units': 6, 'rerank_units': 1}}
  ```

  ```javascript JavaScript
  {
    result: { 
      hits: [ 
        {
          _id: 'rec3',
          _score: 0.004399413242936134,
          fields: {
            category: 'immune system',
            chunk_text: 'Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.'
          }
        },
        {
          _id: 'rec4',
          _score: 0.0029235430993139744,
          fields: {
            category: 'endocrine system',
            chunk_text: 'The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.'
          }
        }
      ]
    },
    usage: { 
      readUnits: 6, 
      embedTotalTokens: 8,
      rerankUnits: 1 
    }
  }
  ```

  ```java Java
  class SearchRecordsResponse {
      result: class SearchRecordsResponseResult {
          hits: [class Hit {
              id: rec3
              score: 0.004399413242936134
              fields: {category=immune system, chunk_text=Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.}
              additionalProperties: null
          }, class Hit {
              id: rec4
              score: 0.0029235430993139744
              fields: {category=endocrine system, chunk_text=The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.}
              additionalProperties: null
          }]
          additionalProperties: null
      }
      usage: class SearchUsage {
          readUnits: 6
          embedTotalTokens: 13
          rerankUnits: 1
          additionalProperties: null
      }
      additionalProperties: null
  }
  ```

  ```go Go
  {
    "result": {
      "hits": [
        {
          "_id": "rec3",
          "_score": 0.13683891,
          "fields": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        {
          "_id": "rec4",
          "_score": 0.0029235430993139744,
          "fields": {
            "category": "endocrine system",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 8,
      "rerank_units": 1
    }
  }
  ```

  ```csharp C#
  {
    "result": {
      "hits": [
        {
          "_id": "rec3",
          "_score": 0.004399413242936134,
          "fields": {
            "category": "immune system",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        },
        {
          "_id": "rec4",
          "_score": 0.0029121784027665854,
          "fields": {
            "category": "endocrine system",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
          }
        }
      ]
    },
    "usage": {
      "read_units": 6,
      "embed_total_tokens": 8,
      "rerank_units": 1
    }
  }
  ```

  ```json curl
  {
      "result": {
          "hits": [
              {
                  "_id": "rec3",
                  "_score": 0.004433765076100826,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec4",
                  "_score": 0.0029121784027665854,
                  "fields": {
                      "category": "endocrine system",
                      "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
                  }
              }
          ]
      },
      "usage": {
          "embed_total_tokens": 8,
          "read_units": 6,
          "rerank_units": 1
      }
  }
  ```
</CodeGroup>

## Standalone reranking

To rerank initial results as a standalone operation, use the [`rerank`](/reference/api/latest/inference/rerank) operation with the [hosted reranking model](#reranking-models) you want to use, the query results and the query, the number of ranked results to return, the field to use for reranking, and any other model-specific parameters.

For example, the following code uses the hosted `bge-reranker-v2-m3` model to rerank the values of the `documents.chunk_text` fields based on their relevance to the query and return only the 2 most relevant documents, along with their score:

<CodeGroup>
  ```python Python
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  ranked_results = pc.inference.rerank(
      model="bge-reranker-v2-m3",
      query="What is AAPL's outlook, considering both product launches and market conditions?",
      documents=[
          {"id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
          {"id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
          {"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."},
      ],
      top_n=2,
      rank_fields=["chunk_text"],
      return_documents=True,
      parameters={
          "truncate": "END"
      }
  )

  print(ranked_results)
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const rerankingModel = 'bge-reranker-v2-m3';

  const query = "What is AAPL's outlook, considering both product launches and market conditions?";

  const documents = [
    { id: 'vec2', chunk_text: "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market." },
    { id: 'vec3', chunk_text: "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production." },
    { id: 'vec1', chunk_text: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones." },
  ];

  const rerankOptions = {
    topN: 2,
    rankFields: ['chunk_text'],
    returnDocuments: true,
    parameters: {
      truncate: 'END'
    }, 
  };

  const rankedResults = await pc.inference.rerank(
    rerankingModel,
    query,
    documents,
    rerankOptions
  );

  console.log(rankedResults);
  ```

  ```java Java
  import io.pinecone.clients.Inference;
  import io.pinecone.clients.Pinecone;
  import org.openapitools.inference.client.model.RerankResult;
  import org.openapitools.inference.client.ApiException;

  import java.util.*;

  public class RerankExample {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          Inference inference = pc.getInferenceClient();

          // The model to use for reranking
          String model = "bge-reranker-v2-m3";

          // The query to rerank documents against
          String query = "What is AAPL's outlook, considering both product launches and market conditions?";

          // Add the documents to rerank
          List<Map<String, Object>> documents = new ArrayList<>();
          Map<String, Object> doc1 = new HashMap<>();
          doc1.put("id", "vec2");
          doc1.put("chunk_text", "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.");
          documents.add(doc1);

          Map<String, Object> doc2 = new HashMap<>();
          doc2.put("id", "vec3");
          doc2.put("chunk_text", "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production");
          documents.add(doc2);

          Map<String, Object> doc3 = new HashMap<>();
          doc3.put("id", "vec1");
          doc3.put("chunk_text", "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.");
          documents.add(doc3);

          // The fields to rank the documents by. If not provided, the default is "text"
          List<String> rankFields = Arrays.asList("chunk_text");

          // The number of results to return sorted by relevance. Defaults to the number of inputs
          int topN = 2;

          // Whether to return the documents in the response
          boolean returnDocuments = true;

          // Additional model-specific parameters for the reranker
          Map<String, Object> parameters = new HashMap<>();
          parameters.put("truncate", "END");

          // Send ranking request
          RerankResult result = inference.rerank(model, query, documents, rankFields, topN, returnDocuments, parameters);

          // Get ranked data
          System.out.println(result.getData());
      }
  }
  ```

  ```go Go
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	rerankModel := "bge-reranker-v2-m3"
  	topN := 2
  	returnDocuments := true
  	documents := []pinecone.Document{
  		{"id": "vec2", "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
  		{"id": "vec3", "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
  		{"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."},
  	}

  	ranking, err := pc.Inference.Rerank(ctx, &pinecone.RerankRequest{
  		Model:           rerankModel,
  		Query:           "What is AAPL's outlook, considering both product launches and market conditions?",
  		ReturnDocuments: &returnDocuments,
  		TopN:            &topN,
  		RankFields:      &[]string{"chunk_text"},
  		Documents:       documents,
  	})
  	if err != nil {
  		log.Fatalf("Failed to rerank: %v", err)
  	}
  	fmt.Printf(prettifyStruct(ranking))
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // Add the documents to rerank
  var documents = new List<Dictionary<string, object?>>
  {
      new()
      {
          ["id"] = "vec2",
          ["chunk_text"] = "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
      },
      new()
      {
          ["id"] = "vec3",
          ["chunk_text"] = "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."
      },
      new()
      {
          ["id"] = "vec1",
          ["chunk_text"] = "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
      }
  };

  // The fields to rank the documents by. If not provided, the default is "text"
  var rankFields = new List<string> { "chunk_text" };

  // Additional model-specific parameters for the reranker
  var parameters = new Dictionary<string, object>
  {
      ["truncate"] = "END"
  };

  // Send ranking request
  var result = await pinecone.Inference.RerankAsync(
      new RerankRequest
      {
          Model = "bge-reranker-v2-m3",
          Query = "What is AAPL's outlook, considering both product launches and market conditions?",
          Documents = documents,
          RankFields = rankFields,
          TopN = 2,
          ReturnDocuments = true,
          Parameters = parameters
      });

  Console.WriteLine(result);
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/rerank \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -d '{
    "model": "bge-reranker-v2-m3",
    "query": "What is AAPL'\''s outlook, considering both product launches and market conditions?",
    "documents": [
      {"id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
      {"id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
      {"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."}
    ],
    "top_n": 2,
    "rank_fields": ["chunk_text"],
    "return_documents": true,
    "parameters": {
      "truncate": "END"
    }
  }'
  ```
</CodeGroup>

The response looks as follows. For each hit, the \_score represents the relevance of a document to the query, normalized between 0 and 1, with scores closer to 1 indicating higher relevance.

<CodeGroup>
  ```python Python
  RerankResult(
    model='bge-reranker-v2-m3',
    data=[{
      index=0,
      score=0.004166256,
      document={
          id='vec2',
          chunk_text="Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."
      }
    },{
      index=2,
      score=0.0011513996,
      document={
          id='vec1',
          chunk_text='AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.'
      }
    }],
    usage={'rerank_units': 1}
  )
  ```

  ```javascript JavaScript
  {
    model: 'bge-reranker-v2-m3',
    data: [
      { index: 0, score: 0.004166256, document: [id: 'vec2', chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."] },
      { index: 2, score: 0.0011513996, document: [id: 'vec1', chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.'] }
    ],
    usage: { rerankUnits: 1 }
  }
  ```

  ```java Java
  [class RankedDocument {
      index: 0
      score: 0.0063143647
      document: {id=vec2, chunk_text=Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.}
      additionalProperties: null
  }, class RankedDocument {
      index: 2
      score: 0.0011513996
      document: {id=vec1, chunk_text=AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.}
      additionalProperties: null
  }]
  ```

  ```go Go
  {
    "data": [
      {
        "document": {
          "id": "vec2",
          "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
        },
        "index": 0,
        "score": 0.0063143647
      },
      {
        "document": {
          "id": "vec1",
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
        },
        "index": 2,
        "score": 0.0011513996
      }
    ],
    "model": "bge-reranker-v2-m3",
    "usage": {
      "rerank_units": 1
    }
  }
  ```

  ```csharp C#
  {
    "model": "bge-reranker-v2-m3",
    "data": [
      {
        "index": 0,
        "score": 0.006289902,
        "document": {
          "chunk_text": "Analysts suggest that AAPL\u0027s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "id": "vec2"
        }
      },
      {
        "index": 3,
        "score": 0.0011513996,
        "document": {
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          "id": "vec1"
        }
      }
    ],
    "usage": {
      "rerank_units": 1
    }
  }
  ```

  ```json curl
  {
      "model": "bge-reranker-v2-m3",
      "data": [
          {
              "index": 0,
              "document": {
                  "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                  "id": "vec2"
              },
              "score": 0.007606672
          },
          {
              "index": 3,
              "document": {
                  "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                  "id": "vec1"
              },
              "score": 0.0013406205
          }
      ],
      "usage": {
          "rerank_units": 1
      }
  }
  ```
</CodeGroup>

{/* ## Rerank results on the default field

  To [rerank search results](/reference/api/latest/inference/rerank), specify a [supported reranking model](/guides/search/rerank-results#reranking-models), and provide documents and a query as well as other model-specific parameters. By default, Pinecone expects the documents to be in the `documents.text` field. 

  For example, the following request uses the `bge-reranker-v2-m3` reranking model to rerank the values of the `documents.text` field based on their relevance to the query, `"The tech company Apple is known for its innovative products like the iPhone."`.

  <Note>
  With `truncate` set to `"END"`, the input sequence (`query` + `document`) is truncated at the token limit (`1024`); to return an error instead, you'd set `truncate` to `"NONE"` or leave the parameter out.
  </Note>

  <CodeGroup>

  ```python Python
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  result = pc.inference.rerank(
    model="bge-reranker-v2-m3",
    query="The tech company Apple is known for its innovative products like the iPhone.",
    documents=[
        {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
        {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
        {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."},
    ],
    top_n=4,
    return_documents=True,
    parameters={
        "truncate": "END"
    }
  )

  print(result)
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const rerankingModel = 'bge-reranker-v2-m3';

  const query = 'The tech company Apple is known for its innovative products like the iPhone.';

  const documents = [
  { id: 'vec1', text: 'Apple is a popular fruit known for its sweetness and crisp texture.' },
  { id: 'vec2', text: 'Many people enjoy eating apples as a healthy snack.' },
  { id: 'vec3', text: 'Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.' },
  { id: 'vec4', text: 'An apple a day keeps the doctor away, as the saying goes.' },
  ];

  const rerankOptions = {
  topN: 4,
  returnDocuments: true,
  parameters: {
    truncate: 'END'
  }, 
  };

  const response = await pc.inference.rerank(
  rerankingModel,
  query,
  documents,
  rerankOptions
  );

  console.log(response);
  ```

  ```java Java
  import io.pinecone.clients.Inference;
  import io.pinecone.clients.Pinecone;
  import org.openapitools.inference.client.model.RerankResult;
  import org.openapitools.inference.client.ApiException;

  import java.util.*;

  public class RerankExample {
    public static void main(String[] args) throws ApiException {
        Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
        Inference inference = pc.getInferenceClient();

        // The model to use for reranking
        String model = "bge-reranker-v2-m3";

        // The query to rerank documents against
        String query = "The tech company Apple is known for its innovative products like the iPhone.";

        // Add the documents to rerank
        List<Map<String, Object>> documents = new ArrayList<>();
        Map<String, Object> doc1 = new HashMap<>();
        doc1.put("id", "vec1");
        doc1.put("text", "Apple is a popular fruit known for its sweetness and crisp texture.");
        documents.add(doc1);

        Map<String, Object> doc2 = new HashMap<>();
        doc2.put("id", "vec2");
        doc2.put("text", "Many people enjoy eating apples as a healthy snack.");
        documents.add(doc2);

        Map<String, Object> doc3 = new HashMap<>();
        doc3.put("id", "vec3");
        doc3.put("text", "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.");
        documents.add(doc3);

        Map<String, Object> doc4 = new HashMap<>();
        doc4.put("id", "vec4");
        doc4.put("text", "An apple a day keeps the doctor away, as the saying goes.");
        documents.add(doc4);

        // The fields to rank the documents by. If not provided, the default is "text"
        List<String> rankFields = Arrays.asList("text");

        // The number of results to return sorted by relevance. Defaults to the number of inputs
        int topN = 4;

        // Whether to return the documents in the response
        boolean returnDocuments = true;

        // Additional model-specific parameters for the reranker
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("truncate", "END");

        // Send ranking request
        RerankResult result = inference.rerank(model, query, documents, rankFields, topN, returnDocuments, parameters);

        // Get ranked data
        System.out.println(result.getData());
    }
  }
  ```

  ```go Go
  package main

  import (
    "context"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    rerankModel := "bge-reranker-v2-m3"
    topN := 4
    returnDocuments := true
    documents := []pinecone.Document{
        {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
        {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
        {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."},
    }

    ranking, err := pc.Inference.Rerank(ctx, &pinecone.RerankRequest{
        Model:           rerankModel,
        Query:           "The tech company Apple is known for its innovative products like the iPhone.",
        ReturnDocuments: &returnDocuments,
        TopN:            &topN,
        RankFields:      &[]string{"text"},
        Documents:       documents,
    })
    if err != nil {
        log.Fatalf("Failed to rerank: %v", err)
    }
    fmt.Printf("Rerank result: %+v\n", ranking)
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // The model to use for reranking
  var model = "bge-reranker-v2-m3";

  // The query to rerank documents against
  var query = "The tech company Apple is known for its innovative products like the iPhone.";

  // Add the documents to rerank
  var documents = new List<Dictionary<string, object>>
  {
    new()
    {
        ["id"] = "vec1",
        ["my_field"] = "Apple is a popular fruit known for its sweetness and crisp texture."
    },
    new()
    {
        ["id"] = "vec2",
        ["my_field"] = "Many people enjoy eating apples as a healthy snack."
    },
    new()
    {
        ["id"] = "vec3",
        ["my_field"] =
            "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
    },
    new()
    {
        ["id"] = "vec4",
        ["my_field"] = "An apple a day keeps the doctor away, as the saying goes."
    }
  };

  // The fields to rank the documents by. If not provided, the default is "text"
  var rankFields = new List<string> { "my_field" };

  // The number of results to return sorted by relevance. Defaults to the number of inputs
  int topN = 4;

  // Whether to return the documents in the response
  bool returnDocuments = true;

  // Additional model-specific parameters for the reranker
  var parameters = new Dictionary<string, object>
  {
    ["truncate"] = "END"
  };

  // Send ranking request
  var result = await pinecone.Inference.RerankAsync(
    new RerankRequest
    {
        Model = model,
        Query = query,
        Documents = documents,
        RankFields = rankFields,
        TopN = topN,
        ReturnDocuments = true,
        Parameters = parameters
    });

  Console.WriteLine(result);
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/rerank \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-API-Version: 2025-04" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -d '{
  "model": "bge-reranker-v2-m3",
  "query": "The tech company Apple is known for its innovative products like the iPhone.",
  "return_documents": true,
  "top_n": 4,
  "documents": [
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."}
  ],
  "parameters": {
    "truncate": "END"
  }
  }'
  ```


  </CodeGroup>

  The returned object contains documents with relevance scores:

  <Note>
  Normalized between 0 and 1, the `score` represents the relevance of a passage to the query, with scores closer to 1 indicating higher relevance.
  </Note>

  <CodeGroup>

  ```python Python
  RerankResult(
  model='bge-reranker-v2-m3',
  data=[
    { index=2, score=0.48357219,
      document={id="vec3", text="Apple Inc. has re..."} },
    { index=0, score=0.048405956,
      document={id="vec1", text="Apple is a popula..."} },
    { index=3, score=0.007846239,
      document={id="vec4", text="An apple a day ke..."} },
    { index=1, score=0.0006563728,
      document={id="vec2", text="Many people enjoy..."} }
  ],
  usage={'rerank_units': 1}
  )
  ```

  ```javascript JavaScript
  {
  model: 'bge-reranker-v2-m3',
  data: [
    { index: 2, score: 0.48357219, document: [Object] },
    { index: 0, score: 0.048405956, document: [Object] },
    { index: 3, score: 0.007846239, document: [Object] },
    { index: 1, score: 0.0006563728, document: [Object] }
  ],
  usage: { rerankUnits: 1 }
  }
  ```

  ```java Java
  [class RankedDocument {
    index: 2
    score: 0.48357219
    document: {id=vec3, text=Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.}
    additionalProperties: null
  }, class RankedDocument {
    index: 0
    score: 0.048405956
    document: {id=vec1, text=Apple is a popular fruit known for its sweetness and crisp texture.}
    additionalProperties: null
  }, class RankedDocument {
    index: 3
    score: 0.007846239
    document: {id=vec4, text=An apple a day keeps the doctor away, as the saying goes.}
    additionalProperties: null
  }, class RankedDocument {
    index: 1
    score: 0.0006563728
    document: {id=vec2, text=Many people enjoy eating apples as a healthy snack.}
    additionalProperties: null
  }]
  ```

  ```go Go
  Rerank result: {
  "data": [
    {
      "document": {
        "id": "vec3",
        "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
      },
      "index": 2,
      "score": 0.48357219
    },
    {
      "document": {
        "id": "vec1",
        "text": "Apple is a popular fruit known for its sweetness and crisp texture."
      },
      "index": 0,
      "score": 0.048405956
    },
    {
      "document": {
        "id": "vec4",
        "text": "An apple a day keeps the doctor away, as the saying goes."
      },
      "index": 3,
      "score": 0.007846239
    },
    {
      "document": {
        "id": "vec2",
        "text": "Many people enjoy eating apples as a healthy snack."
      },
      "index": 1,
      "score": 0.0006563728
    }
  ],
  "model": "bge-reranker-v2-m3",
  "usage": {
    "rerank_units": 1
  }
  }
  ```

  ```csharp C#
  {
  "model": "bge-reranker-v2-m3",
  "data": [
    {
      "index": 2,
      "score": 0.48357219,
      "document": {
        "id": "vec3",
        "my_field": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
      }
    },
    {
      "index": 0,
      "score": 0.048405956,
      "document": {
        "id": "vec1",
        "my_field": "Apple is a popular fruit known for its sweetness and crisp texture."
      }
    },
    {
      "index": 3,
      "score": 0.007846239,
      "document": {
        "id": "vec4",
        "my_field": "An apple a day keeps the doctor away, as the saying goes."
      }
    },
    {
      "index": 1,
      "score": 0.0006563728,
      "document": {
        "id": "vec2",
        "my_field": "Many people enjoy eating apples as a healthy snack."
      }
    }
  ],
  "usage": {
    "rerank_units": 1
  }
  }
  ```

  ```JSON curl
  {
  "data":[
    {
      "index":2,
      "document":{
        "id":"vec3",
        "text":"Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
      },
      "score":0.47654688
    },
    {
      "index":0,
      "document":{
        "id":"vec1",
        "text":"Apple is a popular fruit known for its sweetness and crisp texture."
      },
      "score":0.047963805
    },
    {
      "index":3,
      "document":{
        "id":"vec4",
        "text":"An apple a day keeps the doctor away, as the saying goes."
      },
      "score":0.007587992
    },
    {
      "index":1,
      "document":{
        "id":"vec2",
        "text":"Many people enjoy eating apples as a healthy snack."
      },
      "score":0.0006491712
    }
  ],
  "usage":{
    "rerank_units":1
  }
  }
  ```


  </CodeGroup>

  ## Rerank results on a custom field

  To [rerank results](/reference/api/latest/inference/rerank) on a field other than `documents.text`, provide the `rank_fields` parameter to specify the fields on which to rerank. 

  <Note>
  The [`bge-reranker-v2-m3`](#bge-reranker-v2-m3) and [`pinecone-rerank-v0`](#pinecone-rerank-v0) models support only a single rerank field. [`cohere-rerank-3.5`](#cohere-rerank-3-5) supports multiple rerank fields, ranked based on the order of the fields specified.
  </Note> 

  For example, the following request reranks documents based on the values of the `documents.my_field` field:

  <CodeGroup>

  ```python Python
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  result = pc.inference.rerank(
    model="bge-reranker-v2-m3",
    query="The tech company Apple is known for its innovative products like the iPhone.",
    documents=[
        {"id": "vec1", "my_field": "Apple is a popular fruit known for its sweetness and crisp texture."},
        {"id": "vec2", "my_field": "Many people enjoy eating apples as a healthy snack."},
        {"id": "vec3", "my_field": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {"id": "vec4", "my_field": "An apple a day keeps the doctor away, as the saying goes."},
    ],
    rank_fields=["my_field"],
    top_n=4,
    return_documents=True,
    parameters={
        "truncate": "END"
    }
  )
  ```

  ```javascript JavaScript
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const rerankingModel = 'bge-reranker-v2-m3';

  const query = 'The tech company Apple is known for its innovative products like the iPhone.';

  const documents = [
  { id: 'vec1', my_field: 'Apple is a popular fruit known for its sweetness and crisp texture.' },
  { id: 'vec2', my_field: 'Many people enjoy eating apples as a healthy snack.' },
  { id: 'vec3', my_field: 'Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.' },
  { id: 'vec4', my_field: 'An apple a day keeps the doctor away, as the saying goes.' },
  ];

  const rerankOptions = {
  rankFields: ['my_field'],
  topN: 4,
  returnDocuments: true,
  parameters: {
    truncate: "END"
  }, 
  };

  const response = await pc.inference.rerank(
  rerankingModel,
  query,
  documents,
  rerankOptions
  );

  console.log(response);
  ```

  ```java Java
  import io.pinecone.clients.Inference;
  import io.pinecone.clients.Pinecone;
  import org.openapitools.inference.client.model.RerankResult;
  import org.openapitools.inference.client.ApiException;

  import java.util.*;

  public class RerankExample {
    public static void main(String[] args) throws ApiException {
        Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
        Inference inference = pc.getInferenceClient();

        // The model to use for reranking
        String model = "bge-reranker-v2-m3";

        // The query to rerank documents against
        String query = "The tech company Apple is known for its innovative products like the iPhone.";

        // Add the documents to rerank
        List<Map<String, String>> documents = new ArrayList<>();
        Map<String, String> doc1 = new HashMap<>();
        doc1.put("id", "vec1");
        doc1.put("my_field", "Apple is a popular fruit known for its sweetness and crisp texture.");
        documents.add(doc1);

        Map<String, String> doc2 = new HashMap<>();
        doc2.put("id", "vec2");
        doc2.put("my_field", "Many people enjoy eating apples as a healthy snack.");
        documents.add(doc2);

        Map<String, String> doc3 = new HashMap<>();
        doc3.put("id", "vec3");
        doc3.put("my_field", "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.");
        documents.add(doc3);

        Map<String, String> doc4 = new HashMap<>();
        doc4.put("id", "vec4");
        doc4.put("my_field", "An apple a day keeps the doctor away, as the saying goes.");
        documents.add(doc4);

        // The fields to rank the documents by. If not provided, the default is "text"
        List<String> rankFields = Arrays.asList("my_field");

        // The number of results to return sorted by relevance. Defaults to the number of inputs
        int topN = 2;

        // Whether to return the documents in the response
        boolean returnDocuments = true;

        // Additional model-specific parameters for the reranker
        Map<String, String> parameters = new HashMap<>();
        parameters.put("truncate", "END");

        // Send ranking request
        RerankResult result = inference.rerank(model, query, documents, rankFields, topN, returnDocuments, parameters);

        // Get ranked data
        System.out.println(result.getData());
    }
  }
  ```

  ```go Go
  package main

  import (
    "context"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    rerankModel := "bge-reranker-v2-m3"
    topN := 4
    returnDocuments := true
    documents := []pinecone.Document{
        {"id": "vec1", "my_field": "Apple is a popular fruit known for its sweetness and crisp texture."},
        {"id": "vec2", "my_field": "Many people enjoy eating apples as a healthy snack."},
        {"id": "vec3", "my_field": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {"id": "vec4", "my_field": "An apple a day keeps the doctor away, as the saying goes."},
    }

    ranking, err := pc.Inference.Rerank(ctx, &pinecone.RerankRequest{
        Model:           rerankModel,
        Query:           "The tech company Apple is known for its innovative products like the iPhone.",
        ReturnDocuments: &returnDocuments,
        TopN:            &topN,
        RankFields:      &[]string{"my_field"},
        Documents:       documents,
    })
    if err != nil {
        log.Fatalf("Failed to rerank: %v", err)
    }
    fmt.Printf("Rerank result: %+v\n", ranking)
  }
  ```

  ```csharp C#
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // The model to use for reranking
  var model = "bge-reranker-v2-m3";

  // The query to rerank documents against
  var query = "The tech company Apple is known for its innovative products like the iPhone.";

  // Add the documents to rerank
  var documents = new List<Dictionary<string, string>>
  {
    new()
    {
        ["id"] = "vec1",
        ["my_field"] = "Apple is a popular fruit known for its sweetness and crisp texture."
    },
    new()
    {
        ["id"] = "vec2",
        ["my_field"] = "Many people enjoy eating apples as a healthy snack."
    },
    new()
    {
        ["id"] = "vec3",
        ["my_field"] =
            "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
    },
    new()
    {
        ["id"] = "vec4",
        ["my_field"] = "An apple a day keeps the doctor away, as the saying goes."
    }
  };

  // The fields to rank the documents by. If not provided, the default is "text"
  var rankFields = new List<string> { "my_field" };

  // The number of results to return sorted by relevance. Defaults to the number of inputs
  int topN = 2;

  // Whether to return the documents in the response
  bool returnDocuments = true;

  // Additional model-specific parameters for the reranker
  var parameters = new Dictionary<string, object>
  {
    ["truncate"] = "END"
  };

  // Send ranking request
  var result = await pinecone.Inference.RerankAsync(
    new RerankRequest
    {
        Model = model,
        Query = query,
        Documents = documents,
        RankFields = rankFields,
        TopN = topN,
        ReturnDocuments = true,
        Parameters = parameters
    });

  // Get ranked data
  var data = result.Data;

  Console.WriteLine(data);
  ```

  ```shell curl
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/rerank" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-API-Version: 2025-04" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -d '{
  "model": "bge-reranker-v2-m3",
  "query": "The tech company Apple is known for its innovative products like the iPhone.",
  "return_documents": true,
  "top_n": 4,
  "rank_fields": ["my_field"],
  "documents": [
    {"id": "vec1", "my_field": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "my_field": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec3", "my_field": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec4", "my_field": "An apple a day keeps the doctor away, as the saying goes."}
  ],
  "parameters": {
    "truncate": "END"
  }
  }'
  ```

  </CodeGroup> */}

## Reranking models

Pinecone hosts several reranking models so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.

The following reranking models are hosted by Pinecone.

<Note>
  To understand how cost is calculated for reranking, see [Reranking cost](/guides/manage-cost/understanding-cost#reranking). To get model details via the API, see [List models](/reference/api/latest/inference/list_models) and [Describe a model](/reference/api/latest/inference/describe_model).
</Note>

<AccordionGroup>
  <Accordion title="cohere-rerank-3.5">
    <PaidOnly />

    [`cohere-rerank-3.5`](/models/cohere-rerank-3.5) is Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.

    **Details**

    * Modality: Text
    * Max tokens per query and document pair: 40,000
    * Max documents: 200

    For rate limits, see [Rerank requests per minute](/reference/api/database-limits#rerank-requests-per-minute-per-model) and [Rerank request per month](/reference/api/database-limits#rerank-requests-per-month-per-model).

    **Parameters**

    The `cohere-rerank-3.5` model supports the following parameters:

    | Parameter            | Type             | Required/Optional | Description                                                                                                                             |            |
    | :------------------- | :--------------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
    | `max_chunks_per_doc` | integer          | Optional          | Long documents will be automatically truncated to the specified number of chunks. Accepted range: `1 - 3072`.                           |            |
    | `rank_fields`        | array of strings | Optional          | The fields to use for reranking. The model reranks based on the order of the fields specified (e.g., `["field1", "field2", "field3"]`). | `["text"]` |
  </Accordion>

  <Accordion title="bge-reranker-v2-m3">
    [`bge-reranker-v2-m3`](/models/bge-reranker-v2-m3) is a high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs).

    **Details**

    * Modality: Text
    * Max tokens per query and document pair: 1024
    * Max documents: 100

    For rate limits, see [Rerank requests per minute](/reference/api/database-limits#rerank-requests-per-minute-per-model) and [Rerank request per month](/reference/api/database-limits#rerank-requests-per-month-per-model).

    **Parameters**

    The `bge-reranker-v2-m3` model supports the following parameters:

    | Parameter     | Type             | Required/Optional | Description                                                                                                                                                                                                                                    | Default    |
    | :------------ | :--------------- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
    | `truncate`    | string           | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `NONE`     |
    | `rank_fields` | array of strings | Optional          | The field to use for reranking. The model supports only a single rerank field.                                                                                                                                                                 | `["text"]` |
  </Accordion>

  <Accordion title="pinecone-rerank-v0">
    <PP />

    [`pinecone-rerank-v0`](/models/pinecone-rerank-v0) is a state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs).

    **Details**

    * Modality: Text
    * Max tokens per query and document pair: 512
    * Max documents: 100

    For rate limits, see [Rerank requests per minute](/reference/api/database-limits#rerank-requests-per-minute-per-model) and [Rerank request per month](/reference/api/database-limits#rerank-requests-per-month-per-model).

    **Parameters**

    The `pinecone-rerank-v0` model supports the following parameters:

    | Parameter     | Type             | Required/Optional | Description                                                                                                                                                                                                                                    | Default    |
    | :------------ | :--------------- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
    | `truncate`    | string           | Optional          | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END`      |
    | `rank_fields` | array of strings | Optional          | The field to use for reranking. The model supports only a single rerank field.                                                                                                                                                                 | `["text"]` |
  </Accordion>
</AccordionGroup>