# RESTful API of the Dictionary of the Peoples of the Karachay-Cherkess Republic.

[Документация на русском](https://github.com/Dark04072006/kchr-dictionary-rest-api/blob/main/docs/README.ru.md)

## Technical advantages of the project:

1. **Clean Architecture**: Principles from Robert Martin's Clean Architecture (`Uncle Bob`) are used, facilitating easy maintenance and code flexibility.

2. **Application of some Domain-Driven Design (DDD) principles**: Utilizing DDD principles helps to identify key business entities and improves the modularity of the application.

3. **Usage of asynchronous libraries and frameworks**: The project employs asynchronous libraries and frameworks, enabling high performance and efficient resource utilization.

<!-- Installation -->

## Installation (Linux)

### 1. Cloning the repository

```shell
git clone https://github.com/Dark04072006/kchr-dictionary-rest-api.git
```

### 2. Navigate to the kchr-dictionary-rest-api directory

```shell
cd kchr-dictionary-rest-api
```

### 3. Creating a virtual environment

```shell
python3 -m venv .venv
```

### 4. Activating the virtual environment

```shell
source .venv/bin/activate
```

### 5. Installing dependencies

```shell
pip install -e .
```

#### You can also install linters or testing tools by entering the following command

```shell
pip install -e .[lint,testing]
```

### 6. Setting up environment variables

#### Only one environment variable is required for running: `DATABASE_URI`

By default, it is set to `sqlite+aiosqlite:///assets/dictionary.db`. If you want to set your own value, execute the following command

```shell
export DATABASE_URI=YOUR_DICTIONARY_DB_URI
```

### 7. Running the web API

#### Running in development mode

1. Set permissions for the script

```shell
chmod +x scripts/start.dev.sh
```

2. Run the script

```bash
scripts/start.dev.sh
```

#### Running in production mode

1. Set permissions for the script

```shell
chmod +x scripts/start.prod.sh
```

2. Run the script

```shell
scripts/start.prod.sh
```

## License

See the [LICENSE](https://github.com/Dark04072006/kchr-dictionary-rest-api/blob/main/LICENSE.md) file for license rights and limitations (MIT).

### Issues

If you encounter any issues with the project or have any suggestions for improvements, please feel free to report them by [creating an issue](https://github.com/Dark04072006/kchr-dictionary-rest-api/issues) in the GitHub repository. We welcome your feedback!

### Pull Requests

We encourage contributions from the community! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they're properly tested.
4. Submit a pull request (PR) to the `dev` branch of the original repository.
5. Provide a detailed description of your changes in the PR description.

We appreciate your contributions!

### Contact

If you have any questions, suggestions, or feedback regarding this project, feel free to contact the author:

- **Author:** Alim Abrekov
- **Email:** Abrekovalim38702@gmail.com
- **GitHub:** [https://github.com/Dark04072006](https://github.com/Dark04072006)
- **Telegram:** [https://t.me/some_usernamexD](https://t.me/some_usernamexD)

Stay in touch!
