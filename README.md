# shai 🤖

AI-powered shell command suggestions

## Overview

`shai` is a command-line tool that converts natural language into shell commands using AI. Simply describe what you want to do, and `shai` will suggest the appropriate commands.
You can use OpenAI or a local LLM as long as it follows the same format and supports the structured output feature. vLLM models are tested and supported.

## Installation

### Using pip

```bash
pip install shai
```

## Quick Start

First, set your model to use:

```bash
export SHAI_BASE_URL='model-host'
export SHAI_MODEL_NAME='model-name-to-use'
export SHAI_API_KEY='your-api-key'
export SHAI_DEFAULT_SUGGESTIONS=2
```

Then use `shai`:

```bash
shai run docker test
```

## Usage

### Basic Usage

```bash
shai "create a new python virtual environment" -n 2
```

### Examples

1. Docker operations:

```bash
$ shai run nginx container with port 80
1. docker run -p 80:80 nginx
2. docker run -d -p 80:80 nginx
Choose a command to execute (or 0 to cancel):
```

2. File operations:

```bash
$ shai find all pdf files in current directory
1. find . -name "*.pdf"
2. find . -type f -name "*.pdf"
Choose a command to execute (or 0 to cancel):
```

3. Git operations:

```bash
$ shai "undo last git commit"
1. git reset --soft HEAD~1
2. git reset --hard HEAD~1
Choose a command to execute (or 0 to cancel):
```

## Features

- 🌟 Natural language command generation
- 🎯 Multiple command suggestions
- ✅ Command execution confirmation
- 🔄 Interactive command selection
- 🛡️ Safe execution with confirmation
- 📝 Clear and helpful suggestions

## How It Works

1. You describe what you want to do in plain English
2. `shai` sends your request to LLM to generate command suggestions
3. You choose which command to execute
4. `shai` executes the selected command after confirmation

## Requirements

- Python 3.9 or higher
- Running LLM (Local or OpenAI model)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security

- 🔒 Commands are never executed without explicit confirmation
- 🔑 API keys are handled securely via environment variables
- ⚠️ Always review suggested commands before execution

## Limitations

- Requires active internet connection
- Depends on the LLM availability
- May incur API usage costs
- Suggestions may not always be perfect

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- "Attention is all you need" paper
- The Python community for amazing tools and libraries
- All contributors who help improve this project

---

Made with ❤️ by Islam Almersawi
