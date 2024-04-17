# RESTful API of the Dictionary of the Peoples of the Karachay-Cherkess Republic.

[Документация на русском](https://github.com/Dark04072006/kchr-dictionary-rest-api/blob/main/docs/README.ru.md)

## Technical Advantages of the Project:

1. **Clean Architecture**: Robert Martin's (Uncle Bob's) Clean Architecture principles are employed, facilitating code maintenance and flexibility.

2. **Application of Domain-Driven Design (DDD) Principles**: Utilizing DDD principles helps identify key business entities and improves the modularity of the application.

3. **Use of Asynchronous Libraries and Frameworks**: The project utilizes asynchronous libraries and frameworks, ensuring high performance and efficient resource utilization.

<!-- Installation -->

## Installation (Linux)

### 1. Clone the Repository

```shell
git clone https://github.com/Dark04072006/kchr-dictionary-rest-api.git
```

### 2. Navigate to the kchr-dictionary-rest-api directory

```shell
cd kchr-dictionary-rest-api
```

### 3. Create a Virtual Environment

```shell
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

```shell
source .venv/bin/activate
```

### 5. Install Dependencies

```shell
pip install -e .
```

#### You can also install code linting or testing tools by running the following command

```shell
pip install -e .[lint,testing]
```

### 6. Set Up Environment Variables

#### Only one environment variable is required for running: `DATABASE_URI`

By default, it is set to `sqlite+aiosqlite:///assets/dictionary.db`. If you want to set your own value, execute the following command

```shell
export DATABASE_URI=YOUR_DATABASE_URI_FOR_DICTIONARY
```

### 7. Run the Web API

#### Run in Development Mode

1. Set permissions for the script

```shell
chmod +x scripts/start.dev.sh
```

2. Run the script

```bash
scripts/start.dev.sh
```

#### Run in Production Mode

1. Set permissions for the script

```shell
chmod +x scripts/start.prod.sh
```

2. Run the script

```shell
scripts/start.prod.sh
```

## REST API Documentation

#### GET /items

Retrieve a list of dictionary items.

**Description:** This endpoint allows retrieving a list of dictionary items.

**Request Parameters:**

- `limit` (optional): Number of items to display per page. Maximum value: 100. Default: 20.
- `offset` (optional): Offset from the beginning of the list of items. Maximum value: 100. Default: 0.
- `language` (optional): Language in which to retrieve dictionary items. Possible values: "KAR", "CS", "RUSS". Default: null.

**Example Request:**

```http
GET /items?limit=20&offset=0&language=KAR
```

**Example Response:**

```json
{
  "data": [
    {
      "id": 21,
      "original": "абитуриент",
      "translation": "абитуриент || абитуриентский",
      "original_language": "KAR",
      "translation_language": "RUSS"
    },
    {
      "id": 22,
      "original": "аблескин",
      "translation": "<em>текст. </em>аблескин <em>(род шёлковой ткани).</em>",
      "original_language": "KAR",
      "translation_language": "RUSS"
    },
    {
      "id": 23,
      "original": "аблёскюн",
      "translation": "<em>то же, что </em><strong>аблескин</strong>",
      "original_language": "KAR",
      "translation_language": "RUSS"
    }
    // Other dictionary items...
  ]
}
```

#### GET /translations

Search for translations for a given word/phrase.

**Description:** This endpoint allows searching for translations for a given word/phrase.

**Request Parameters:**

- `limit` (optional): Number of items to display per page. Maximum value: 100. Default: 20.
- `offset` (optional): Offset from the beginning of the list of items. Maximum value: 100. Default: 0.
- `original` (required): Word or phrase for which to find translations.
- `original_language` (required): Original language. Possible values: "KAR", "CS", "RUSS".
- `translation_language` (required): Translation language. Possible values: "KAR", "CS", "RUSS".

**Example Request:**

```http
GET /translations?limit=20&offset=0&original=привет&original_language=RUSS&translation_language=KAR
```

**Example Response:**

```json
{
  "data": [
    {
      "id": 42411,
      "original": "неприветливый",
      "translation": "-ая, -ое <strong>1. </strong><i>(неласковый, суровый) </i>хыны, гырхы, дюрген; ~ <strong>человек </strong>хыны адам; <strong>2. </strong><i>(мрачный) </i>къууатсыз, илешсиз, мугур.",
      "original_language": "RUSS",
      "translation_language": "KAR"
    }
    // Other translations...
  ]
}
```

### /health-check/

#### GET /health-check/

Health Check.

**Description:** This endpoint allows checking the state of the application.

**Example Request:**

```http
GET /health-check/
```

**Example Response:**

```json
{
  "status": "Ok"
}
```

You can also utilize the [openapi specification](https://github.com/Dark04072006/kchr-dictionary-rest-api/blob/main/openapi/openapi.json)

## License

See the [LICENSE](https://github.com/Dark04072006/kchr-dictionary-rest-api/blob/main/LICENSE.md) file for license rights and limitations (MIT).

### Issues

If you encounter any issues with the project or have suggestions for improvement, please feel free to report them by [creating an issue](https://github.com/Dark04072006/kchr-dictionary-rest-api/issues) in the GitHub repository. We welcome your feedback!

### Pull Requests

We welcome community contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and ensure they are properly tested.
4. Propose a pull request (PR) to the `dev` branch of the original repository.
5. Provide a detailed description of your changes in the PR description.

We appreciate your contribution!

### Contact

If you have any questions, suggestions, or feedback regarding this project, feel free to contact the author:

- **Author:** Alim Abrekov
- **Email:** Abrekovalim38702@gmail.com
- **GitHub:** [https://github.com/Dark04072006](https

://github.com/Dark04072006)
- **Telegram:** [https://t.me/some_usernamexD](https://t.me/some_usernamexD)

Stay connected!