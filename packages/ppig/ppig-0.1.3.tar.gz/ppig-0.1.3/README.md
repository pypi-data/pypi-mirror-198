# PPIG: A simple AI terminal assistant

Example:

* Input:

```bash
➜ ppig list only directories        

      ls -d */
The command has been copied to the clipboard

➜ 
```

Make sure your device has some sort of clipboard system such as `xclip`. If it doesn't you can install it executing: 

```bash
➜ sudo apt-get install xclip
```

## Config
`ppig` uses OpenAI API. In order to use this API you need to be signed up in OpenAI as well as an API key. ([get it here](https://platform.openai.com/account/api-keys))

Once you have your API key, you have two options:

1. Create a `ppig_cfg.yaml` file in the directory from which you will call `ppig`. Choosing this option you won't be able to use ppig outside of that foler.
2. Create the path `~/.ppig/ppig_cfg.yaml`. Choosing this option you will be able to use ppig from any folder.

In both cases, the `ppig_cfg.yaml` muste be like this:

```YAML
api_key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Replace `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` with your API key.




