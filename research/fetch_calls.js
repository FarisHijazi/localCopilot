await fetch('http://localhost:5001/v1/engines/codegen/completions', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json'
    },
    body: JSON.stringify({
        'prompt': 'def hello',
        'max_tokens': 100,
        'temperature': 0.1,
        'stop': [
            '\n\n'
        ]
    })
}).then(r => r.text())



await fetch('http://localhost:5001/v1/engines/codegen/completions', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json'
    },
    body: JSON.stringify({
        'prompt': '.vscode/**\n.vscode-test/**\nout/test/**\nsrc/**\n.gitignore\n.yarnrc\n**/tsconfig.json\n**/.eslintrc.json\n**/*.map\nfauxpilot/**\n', 'suffix': '',
        'max_tokens': 500,
        'temperature': 0.4,
        'top_p': 1,
        // 'n': 10, // <----- THIS IS THE PROBLEM
        'stop': ['\n\n\n'],
        'logprobs': 2,
        'nwo': 'CodedotAl/code-clippy-vscode',
        'stream': true,
        'extra': {
            'language': 'ignore',
            'next_indent': 0,
            'prompt_tokens': 55,
            'suffix_tokens': 0,
            'force_indent': -1,
            'trim_by_indentation': true
        }
    })
}).then(r => r.text())




console.log(await fetch('http://localhost:5001/chat/completions', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json'
    },
    body: JSON.stringify({
        "prompt": "def hello_wo",
        "suffix": "",
        "max_tokens": 500,
        "temperature": 0.4,
        "top_p": 1,
        // "n": 10,
        "nwo": "FarisHijazi/dotfiles",
        "logprobs": 2,
        "stop": [
            "\n\n\n"
        ],
        "feature_flags": [
            "trim_to_block"
        ],
        "stream": true,
        "extra": {
            "language": "jsonc",
            "next_indent": 4,
            "force_indent": 0
        }
    })
}).then(r => r.text()))
