# Password CLI Option and Confirmation Prompt

Apart from having a prompt, you can make a *CLI option* have a `confirmation_prompt=True`:

{* docs_src/options/password/tutorial001_an.py hl[7] *}

And the CLI program will ask for confirmation:

<div class="termy">

```console
$ python main.py Camila

// It prompts for the email
# Email: $ camila@example.com
# Repeat for confirmation: $ camila@example.com

Hello Camila, your email is camila@example.com
```

</div>

## A Password prompt

When receiving a password, it is very common (in most shells) to not show anything on the screen while typing the password.

The program will still receive the password, but nothing will be shown on screen, not even `****`.

You can achieve the same using `hide_input=True`.

And if you combine it with `confirmation_prompt=True` you can easily receive a password with double confirmation:

{* docs_src/options/password/tutorial002_an.py hl[8] *}

Check it:

<div class="termy">

```console
$ python main.py Camila

// It prompts for the password, but doesn't show anything when you type
# Password: $
# Repeat for confirmation: $

// Let's imagine the password typed was "cligeniusrocks"
Hello Camila. Doing something very secure with password.
...just kidding, here it is, very insecure: cligeniusrocks
```

</div>
