# Hermes Profile + Distinct Slack Bot Onboarding

Use this after role design when a specialist must appear as a separate Slack identity.

## Architecture

A complete worker has two separate objects:

1. Hermes profile — SOUL, memory, skills, config, sessions, credentials.
2. Slack app — display name, bot user, Socket Mode connection, OAuth scopes.

One Slack app exposes one bot identity. Two distinct visible bots require two Slack apps and separate `xoxb-...` and `xapp-...` credentials.

## Profile workflow

```bash
hermes profile create <handle> --description "<one or two sentence routing description>"
```

Prefer a lowercase alphanumeric handle. Use a fresh profile unless cloning is explicitly justified. Do not use `--clone-all` from an executive assistant profile merely for convenience.

Create the profile’s SOUL.md and ROLE.md, configure its provider/model through Hermes CLI, then test inference:

```bash
hermes -p <handle> -z "State your name, role, and reporting line in one sentence."
```

The test must return the designed identity. If it reports no provider, configure the profile before continuing; profile creation alone is not operational readiness.

## Slack manifest

Run interactive gateway setup before the final branded manifest, or regenerate the branded manifest afterward. `gateway setup` may write a default manifest and overwrite an earlier custom `--name` / `--description` file.

```bash
hermes -p <handle> slack manifest \
  --agent-view \
  --name "<Display Name>" \
  --description "<short role description>" \
  --write
```

Read back or inspect the generated manifest and verify its display name before giving it to the operator.

In Slack:

1. Open `https://api.slack.com/apps`.
2. Create New App → From an app manifest.
3. Choose the workspace and paste/upload the generated manifest.
4. Enable/confirm Socket Mode.
5. Create an App-Level Token with `connections:write` (`xapp-...`).
6. Install the app to the workspace and copy its Bot User OAuth Token (`xoxb-...`).
7. Enable App Home messages if DMs are required.
8. Record the allowed human Slack Member IDs.

Do not request tokens in a shared chat. Have the operator enter them via a secure local terminal, dashboard secret input, or approved secret manager.

If the operator pastes credentials into chat anyway:

1. Never quote, summarize, or echo either token in later messages.
2. Feed them only into a masked interactive setup prompt (PTY) or a secret manager; do not place them in a shell command line where process listings may expose them.
3. Recommend deleting the credential-bearing message.
4. If the chat was shared, logged broadly, or its access is uncertain, recommend rotating both the bot and app tokens and then updating the profile.
5. Do not claim the tokens are safe merely because the conversation is a DM.

The Slack Member ID and home channel ID are routing identifiers rather than bearer credentials. They may be copied from an existing trusted profile when the same operator and destination apply, but extract only those named values—never print or read back the existing profile's tokens.

## Bind credentials to the right profile

```bash
hermes -p <handle> gateway setup
```

Select Slack and configure the new app’s tokens and allowlist. Verify the resulting configuration belongs to the specialist profile, not the chief-of-staff profile.

## Gateway topology

Choose deliberately:

- **One process per profile:** strongest isolation and independent restart; default for a small crew.
- **Multiplexing gateway:** useful in containers or for many low-traffic profiles; the default gateway serves secondary profiles with their own credentials.

Do not run both a profile’s standalone gateway and a multiplexer serving that profile; that double-binds inbound platforms.

On container images where `gateway setup` reports that service installation is unsupported, `hermes -p <handle> gateway start` can still launch the profile gateway and record a desired running state. Verify the live result instead of treating an empty command response as success:

```bash
hermes -p <handle> gateway status
```

Then inspect the profile-scoped gateway state or log for all of these signals:

- active profile is the intended handle
- Slack authenticated as the intended `@bot` in the intended workspace
- Socket Mode connected
- `platforms.slack.state` is `connected`

A live process alone is insufficient: it may be running while Slack authentication failed. A connected gateway is still not full conversational verification until an authorized human DM or mention receives the intended persona's reply.

## Slack slash-command collision

Generated manifests register standard Hermes commands. Multiple apps in one workspace can compete for identical command names. For secondary bots, prefer DMs and `@mention` routing, or deliberately remove/namespace duplicate slash commands before installation. Do not discover this only after production rollout.

## End-to-end verification

1. Profile identity probe passes.
2. Gateway reports healthy for the intended profile.
3. Slack shows the intended app display name and bot user.
4. An authorized human sends a DM and receives the specialist persona’s response.
5. A channel mention routes only to the intended bot.
6. Another bot’s token, memory, and sensitive integrations are not present.
7. Restart the gateway and repeat one DM to prove persistence.

Only then report that the Slack bot is fully onboarded.
