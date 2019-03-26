import pytest


def test_regimen(
    mtrain_client, 
    progression_plan,
):
    mouse_id = progression_plan['mouse_meta']['LabTracks_ID']

    assert mtrain_client.get_stage(mouse_id)['name'] == \
        progression_plan['initial_stage'], \
        'not at expected initial stage before progressions'

    for progression in progression_plan['progressions']:
        assert mtrain_client.get_stage(mouse_id) == \
            progression['start_stage'], \
            'start at expected stage'

        mtrain_client.progress(
            mouse_id,
            progression['behavior_session'],
        )

        assert mtrain_client.get_stage(mouse_id)['name'] == \
            progression['end_stage'], \
            'end at expected stage'
