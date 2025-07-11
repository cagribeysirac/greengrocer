#!/bin/bash

BASE_DIR="src/extensions"
TEMPLATE_PATH="templates/django_app_template"

APP_NAME=$1
APP_PATH="${BASE_DIR}/${APP_NAME}"

if [ -z "$APP_NAME" ]; then
    echo "❌ App name is required!"
    echo "Usage: django-startapp <app-name>"
    exit 1
fi

if [ -d "$APP_PATH" ]; then
        echo "⚠️ $APP_PATH already exists!"
        exit 1
    else
        # Create the app directory if it doesn't exist
        mkdir -p "$APP_PATH"
        echo "📁 Folder created: $APP_PATH"
    fi


# Create the app
django-admin startapp "$APP_NAME" "$APP_PATH" --template="$TEMPLATE_PATH"

echo "✅ App '${APP_NAME}' created: $APP_PATH"
