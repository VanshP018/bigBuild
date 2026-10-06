const { getDefaultConfig } = require('expo/metro-config');

// Expo's default Metro config includes workspace-aware resolution for pnpm monorepos.
module.exports = getDefaultConfig(__dirname);