import argparse
import os
from launch import LaunchClient

from launch_image_minimal_example.server import MyRequestSchema, MyResponseSchema  # Defined as part of your server.py


def main(repo, tag, model_bundle_name):
    client = LaunchClient(api_key=os.getenv("LAUNCH_API_KEY"))
    client.create_model_bundle_from_runnable_image_v2(
        model_bundle_name=model_bundle_name,
        request_schema=MyRequestSchema,
        response_schema=MyResponseSchema,
        repository=repo,
        tag=tag,
        command=[
            "dumb-init",
            "--",
            "uvicorn",
            "launch_image_minimal_example.server:app",
            "--port",
            "5005",
            "--host",
            "::",
        ],
        readiness_initial_delay_seconds=120,
        env={},
    )
    client.create_model_endpoint(
        endpoint_name=f"endpoint-{model_bundle_name}",
        model_bundle=model_bundle_name,
        endpoint_type="async",
        min_workers=0,
        max_workers=1,
        per_worker=1,
        memory="3Gi",
        storage="3Gi",
        cpus=3,
        gpus=0,
        # gpu_type="nvidia-ampere-a10",
        update_if_exists=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", "-r", type=str)
    parser.add_argument("--tag", "-t", type=str)
    parser.add_argument("--bundle-name", "-n", type=str)
    args = parser.parse_args()
    main(args.repo, args.tag, args.bundle_name)
