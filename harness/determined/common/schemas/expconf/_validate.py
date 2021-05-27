from typing import Any, Dict, List, Optional

import jsonschema

from determined.common.schemas import extensions, util
from determined.common.schemas.expconf import _gen

_validators = {}  # type: Dict[str, Any]


def make_validator(url: Optional[str] = None, complete = False) -> Any:
    # Use the experiment config schema by default.
    if url is None:
        url = "http://determined.ai/schemas/expconf/v1/experiment.json"

    global _validators
    if url in _validators:
        return _validators[url]

    schema = _gen.schemas[url]

    resolver = jsonschema.RefResolver(
        base_uri=url,
        referrer=schema,
        handlers={"http": lambda url: _gen.schemas[url]},
    )

    validator = jsonschema.Draft7Validator(schema=schema, resolver=resolver)
    ext = {
        "disallowProperties": extensions.disallowProperties,
        "union": extensions.union,
        "checks": extensions.checks,
        "compareProperties": extensions.compareProperties,
        "conditional": extensions.conditional,
        "optionalRef": extensions.optionalRef,
    }
    if complete:
        ext["eventuallyRequired"] = extensions.eventuallyRequired
        ext["eventually"] = extensions.eventually
    print(complete)
    print(ext)

    cls = jsonschema.validators.extend(validator, ext)
    _validators[url] = cls(schema=schema, resolver=resolver)

    return _validators[url]


def sanity_validation_errors(instance: Any, url: Optional[str] = None) -> List[str]:
    validator = make_validator(url)
    return _validate(instance, validator)


def completeness_validation_errors(instance: Any, url: Optional[str] = None) -> List[str]:
    validator = make_validator(complete=True, url=url)
    print(validator)
    return _validate(instance, validator)


def _validate(instance: Any, validator: Any) -> List[str]:
    errors = validator.iter_errors(instance)
    return util.format_validation_errors(errors)


def get_default(url: str, prop: str) -> Any:
    return _gen.schemas[url].get("properties", {}).get(prop, {}).get("default")


def get_schema(url: str) -> Dict:
    return _gen.schemas[url]  # type: ignore
