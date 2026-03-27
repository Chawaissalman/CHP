# Streamlit deployment bundle

This app is ready to deploy to **Streamlit Community Cloud**.

## Files to keep in your GitHub repo

```text
.
├── app.py
├── app_improved_same_structure.py
├── thermo_engine_improved.py
├── requirements.txt
└── .streamlit/
    └── config.toml
```

## Local run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push the files above to a GitHub repository.
2. In Streamlit Community Cloud, create a new app from that repo.
3. Set the **main file path** to `app.py`.
4. In Advanced settings, choose a current supported Python version if needed.
5. Deploy.

## Notes

- `requirements.txt` is the important dependency file for Community Cloud.
- `packages.txt` is **not needed** for this app because there are no extra Linux packages required.
- The wrapper `app.py` exists only to make deployment simpler; the main app logic remains in `app_improved_same_structure.py`.
- If you want, you can also deploy directly with `app_improved_same_structure.py` as the main file instead of `app.py`.
