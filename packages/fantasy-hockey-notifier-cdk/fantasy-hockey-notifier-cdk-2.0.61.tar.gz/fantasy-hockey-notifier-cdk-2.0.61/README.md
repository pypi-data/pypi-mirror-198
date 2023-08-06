# Fantasy Hockey Notifier CDK

> AWS CDK construct to send notifications for adds, drops, and trades in an ESPN Fantasy Hockey league

[![NPM version](https://badge.fury.io/js/fantasy-hockey-notifier-cdk.svg)](https://badge.fury.io/js/fantasy-hockey-notifier-cdk)
[![PyPI version](https://badge.fury.io/py/fantasy-hockey-notifier-cdk.svg)](https://badge.fury.io/py/fantasy-hockey-notifier-cdk)
[![Release](https://github.com/ftalburt/fantasy-hockey-notifier-cdk/actions/workflows/release.yml/badge.svg)](https://github.com/ftalburt/fantasy-hockey-notifier-cdk/actions/workflows/release.yml)

This application checks for and sends notifications about adds, drops, and trades in an ESPN Fantasy Hockey league. All ESPN APIs used are unofficial and undocumented, thus this application may break at some point in the future if ESPN changes the response schema for any of the endpoints. The codebase supports local execution, along with deployment to AWS using [AWS CDK](https://aws.amazon.com/cdk).

## Local Execution

In addition to being consumable as a CDK construct (which is the primary use-case), the project supports local execution for testing purposes.

### Prerequisites for Local Execution

* Node.js 14 or later
* See the [Environment Variables](#environment-variables) section for a list of required and optional variables that should be exported in the shell or set in the .env file
* If using any of the environment variables starting with `AWS_` or ending with `_SSM`, you must configure AWS credentials via a local credentials file or environment variables. See the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for details.

### Shell Commands for Local Execution

```sh
npm ci
npm start
```

## API Reference

See [API.md](./API.md).

## Environment Variables

### Required Variables

`FH_SEASON` or `FH_SEASON_SSM`: The year of the fantasy hockey season (i.e. `2020` for the 2019-2020 season)

`FH_LEAGUE_ID` or `FH_LEAGUE_ID_SSM`: The ID of the ESPN fantasy hockey league (this is displayed in the URL when you go to the `My Team` page) or the path for an SSM parameter with this value (SSM variable takes prescedence if both are specified)

`ESPN_S2_COOKIE` or `ESPN_S2_COOKIE_SSM`: The value of your `espn_s2` cookie to be used for authentication (you can find this by examining stored cookies for espn.com using the Chrome or Firefox developer tools) or the path for an SSM parameter with this value (SSM variable takes prescedence if both are specified)

### Optional Variables

`AWS_SNS_TOPIC_ARN`: The ARN of an existing AWS SNS topic

`AWS_DYNAMO_DB_TABLE_NAME` or `DISCORD_WEBHOOK_SSM`: The name of an existing Dynamo DB table to use for storing last run dates (takes priority over `LAST_RUN_FILE_PATH` if both are set) or the path for an SSM parameter with this value (SSM variable takes prescedence if both are specified)

`DISCORD_WEBHOOK`: A Discord webhook URL

`LAST_RUN_FILE_PATH`: A local file path to use for storing last run dates (defaults to `.lastrun`)

`EARLIEST_DATE`: A unix timestamp in milliseconds to use as the earliest date when looking up transactions

`LATEST_DATE`: A unix timestamp in milliseconds to use as the latest date when looking up transactions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
