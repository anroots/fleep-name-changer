# Fleep Name Changer

Randomly assign oneself middle names in Fleep (Ando "The Silencer" Roots).

## Usage

```
$ docker run -d -e FLEEP_EMAIL=<email> -e FLEEP_PASSWORD=<password> -e NAME_PREFIX=Luke -e NAME_SUFFIX=Skywalker anroots/fleep-name-changer
```

## Environment Variables

- **FLEEP_EMAIL**: Fleep username (email)
- **FLEEP_PASSWORD**: Fleep password
- **SLEEP_DURATION**: Time delay in seconds between each name change
- **NAME_PREFIX**: The first name to use
- **NAME_SUFFIX**: The last name to use

## License

MIT