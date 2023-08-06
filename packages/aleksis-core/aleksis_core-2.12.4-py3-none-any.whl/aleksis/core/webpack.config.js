const fs = require("fs");
const path = require("path");
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const { VueLoaderPlugin } = require("vue-loader");
const ESLintPlugin = require("eslint-webpack-plugin");
const StyleLintPlugin = require("stylelint-webpack-plugin");

module.exports = {
  context: __dirname,
  entry: JSON.parse(fs.readFileSync("./webpack-entrypoints.json")),
  output: {
    path: path.resolve("./webpack_bundles/"),
    filename: "[name]-[hash].js",
    chunkFilename: "[id]-[chunkhash].js",
  },
  plugins: [
    new BundleTracker({ filename: "./webpack-stats.json" }),
    new VueLoaderPlugin(),
    new ESLintPlugin({
      extensions: ["js", "vue"],
    }),
    new StyleLintPlugin({
      files: ["assets/**/*.{vue,htm,html,css,sss,less,scss,sass}"],
    }),
  ],
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: {
          loader: "vue-loader",
          options: {
            transpileOptions: {
              transforms: {
                dangerousTaggedTemplateString: true,
              },
            },
          },
        },
      },
      {
        test: /\.(css)$/,
        use: ["vue-style-loader", "css-loader"],
      },
      {
        test: /\.scss$/,
        use: [
          "vue-style-loader",
          "css-loader",
          {
            loader: "sass-loader",
            options: {
              sassOptions: {
                indentedSyntax: false,
              },
            },
          },
        ],
      },
      {
        test: /\.(graphql|gql)$/,
        exclude: /node_modules/,
        loader: "graphql-tag/loader",
      },
    ],
  },
  optimization: {
    runtimeChunk: "single",
    splitChunks: {
      chunks: "all",
      maxInitialRequests: Infinity,
      minSize: 0,
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name(module) {
            // get the name. E.g. node_modules/packageName/not/this/part.js
            // or node_modules/packageName
            const packageName = module.context.match(
              /[\\/]node_modules[\\/](.*?)([\\/]|$)/
            )[1];

            // npm package names are URL-safe, but some servers don't like @ symbols
            return `npm.${packageName.replace("@", "")}`;
          },
        },
      },
    },
  },
  resolve: {
    modules: [path.resolve("./node_modules")],
    alias: {
      vue$: "vue/dist/vue.esm.js",
    },
  },
};
