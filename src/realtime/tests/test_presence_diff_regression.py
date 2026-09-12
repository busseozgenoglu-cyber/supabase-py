from realtime import AsyncRealtimePresence


def test_presence_diff_continues_after_untracked_leave():
    presence = AsyncRealtimePresence()
    leave_keys = []
    presence.on_leave(lambda key, _current, _left: leave_keys.append(key))

    presence._on_state_event(
        {"bob": {"metas": [{"phx_ref": "ref-bob"}]}}
    )
    presence._on_diff_event(
        {
            "joins": {},
            "leaves": {
                "alice": {"metas": [{"phx_ref": "ref-alice"}]},
                "bob": {"metas": [{"phx_ref": "ref-bob"}]},
            },
        }
    )

    assert presence.state == {}
    assert leave_keys == ["bob"]
