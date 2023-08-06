<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Changelog

## [20.0.0](https://github.com/apache/arrow-datafusion-python/tree/20.0.0) (2023-03-17)

[Full Changelog](https://github.com/apache/arrow-datafusion-python/compare/0.8.0...20.0.0)

**Implemented enhancements:**

- Empty relation bindings [#208](https://github.com/apache/arrow-datafusion-python/pull/208) (jdye64)
- wrap display_name and canonical_name functions [#214](https://github.com/apache/arrow-datafusion-python/pull/214) (jdye64)
- Add PyAlias bindings [#216](https://github.com/apache/arrow-datafusion-python/pull/216) (jdye64)
- Add bindings for scalar_variable [#218](https://github.com/apache/arrow-datafusion-python/pull/218) (jdye64)
- Bindings for LIKE type expressions [#220](https://github.com/apache/arrow-datafusion-python/pull/220) (jdye64)
- Bool expr bindings [#223](https://github.com/apache/arrow-datafusion-python/pull/223) (jdye64)
- Between bindings [#229](https://github.com/apache/arrow-datafusion-python/pull/229) (jdye64)
- Add bindings for GetIndexedField [#227](https://github.com/apache/arrow-datafusion-python/pull/227) (jdye64)
- Add bindings for case, cast, and trycast [#232](https://github.com/apache/arrow-datafusion-python/pull/232) (jdye64)
- add remaining expr bindings [#233](https://github.com/apache/arrow-datafusion-python/pull/233) (jdye64)
- feature: Additional export methods [#236](https://github.com/apache/arrow-datafusion-python/pull/236) (simicd)
- Add Python wrapper for LogicalPlan::Union [#240](https://github.com/apache/arrow-datafusion-python/pull/240) (iajoiner)
- feature: Create dataframe from pandas, polars, dictionary, list or pyarrow Table [#242](https://github.com/apache/arrow-datafusion-python/pull/242) (simicd)
- Add Python wrappers for `LogicalPlan::Join` and `LogicalPlan::CrossJoin` [#246](https://github.com/apache/arrow-datafusion-python/pull/246) (iajoiner)
- feature: Set table name from ctx functions [#260](https://github.com/apache/arrow-datafusion-python/pull/260) (simicd)
- Explain bindings [#264](https://github.com/apache/arrow-datafusion-python/pull/264) (jdye64)
- Extension bindings [#266](https://github.com/apache/arrow-datafusion-python/pull/266) (jdye64)
- Subquery alias bindings [#269](https://github.com/apache/arrow-datafusion-python/pull/269) (jdye64)
- Create memory table [#271](https://github.com/apache/arrow-datafusion-python/pull/271) (jdye64)
- Create view bindings [#273](https://github.com/apache/arrow-datafusion-python/pull/273) (jdye64)
- Re-export Datafusion dependencies [#277](https://github.com/apache/arrow-datafusion-python/pull/277) (jdye64)
- Distinct bindings [#275](https://github.com/apache/arrow-datafusion-python/pull/275) (jdye64)
- Drop table bindings [#283](https://github.com/apache/arrow-datafusion-python/pull/283) (jdye64)
- Bindings for LogicalPlan::Repartition [#285](https://github.com/apache/arrow-datafusion-python/pull/285) (jdye64)
- Expand Rust return type support for Arrow DataTypes in ScalarValue [#287](https://github.com/apache/arrow-datafusion-python/pull/287) (jdye64)

**Documentation updates:**

- docs: Example of calling Python UDF & UDAF in SQL [#258](https://github.com/apache/arrow-datafusion-python/pull/258) (simicd)

**Merged pull requests:**

- Minor docs updates [#210](https://github.com/apache/arrow-datafusion-python/pull/210) (andygrove)
- Empty relation bindings [#208](https://github.com/apache/arrow-datafusion-python/pull/208) (jdye64)
- wrap display_name and canonical_name functions [#214](https://github.com/apache/arrow-datafusion-python/pull/214) (jdye64)
- Add PyAlias bindings [#216](https://github.com/apache/arrow-datafusion-python/pull/216) (jdye64)
- Add bindings for scalar_variable [#218](https://github.com/apache/arrow-datafusion-python/pull/218) (jdye64)
- Bindings for LIKE type expressions [#220](https://github.com/apache/arrow-datafusion-python/pull/220) (jdye64)
- Bool expr bindings [#223](https://github.com/apache/arrow-datafusion-python/pull/223) (jdye64)
- Between bindings [#229](https://github.com/apache/arrow-datafusion-python/pull/229) (jdye64)
- Add bindings for GetIndexedField [#227](https://github.com/apache/arrow-datafusion-python/pull/227) (jdye64)
- Add bindings for case, cast, and trycast [#232](https://github.com/apache/arrow-datafusion-python/pull/232) (jdye64)
- add remaining expr bindings [#233](https://github.com/apache/arrow-datafusion-python/pull/233) (jdye64)
- Pre-commit hooks [#228](https://github.com/apache/arrow-datafusion-python/pull/228) (jdye64)
- Implement new release process [#149](https://github.com/apache/arrow-datafusion-python/pull/149) (andygrove)
- feature: Additional export methods [#236](https://github.com/apache/arrow-datafusion-python/pull/236) (simicd)
- Add Python wrapper for LogicalPlan::Union [#240](https://github.com/apache/arrow-datafusion-python/pull/240) (iajoiner)
- feature: Create dataframe from pandas, polars, dictionary, list or pyarrow Table [#242](https://github.com/apache/arrow-datafusion-python/pull/242) (simicd)
- Fix release instructions [#238](https://github.com/apache/arrow-datafusion-python/pull/238) (andygrove)
- Add Python wrappers for `LogicalPlan::Join` and `LogicalPlan::CrossJoin` [#246](https://github.com/apache/arrow-datafusion-python/pull/246) (iajoiner)
- docs: Example of calling Python UDF & UDAF in SQL [#258](https://github.com/apache/arrow-datafusion-python/pull/258) (simicd)
- feature: Set table name from ctx functions [#260](https://github.com/apache/arrow-datafusion-python/pull/260) (simicd)
- Upgrade to DataFusion 19 [#262](https://github.com/apache/arrow-datafusion-python/pull/262) (andygrove)
- Explain bindings [#264](https://github.com/apache/arrow-datafusion-python/pull/264) (jdye64)
- Extension bindings [#266](https://github.com/apache/arrow-datafusion-python/pull/266) (jdye64)
- Subquery alias bindings [#269](https://github.com/apache/arrow-datafusion-python/pull/269) (jdye64)
- Create memory table [#271](https://github.com/apache/arrow-datafusion-python/pull/271) (jdye64)
- Create view bindings [#273](https://github.com/apache/arrow-datafusion-python/pull/273) (jdye64)
- Re-export Datafusion dependencies [#277](https://github.com/apache/arrow-datafusion-python/pull/277) (jdye64)
- Distinct bindings [#275](https://github.com/apache/arrow-datafusion-python/pull/275) (jdye64)
- build(deps): bump actions/checkout from 2 to 3 [#244](https://github.com/apache/arrow-datafusion-python/pull/244) (dependabot[bot])
- build(deps): bump actions/upload-artifact from 2 to 3 [#245](https://github.com/apache/arrow-datafusion-python/pull/245) (dependabot[bot])
- build(deps): bump actions/download-artifact from 2 to 3 [#243](https://github.com/apache/arrow-datafusion-python/pull/243) (dependabot[bot])
- Use DataFusion 20 [#278](https://github.com/apache/arrow-datafusion-python/pull/278) (andygrove)
- Drop table bindings [#283](https://github.com/apache/arrow-datafusion-python/pull/283) (jdye64)
- Bindings for LogicalPlan::Repartition [#285](https://github.com/apache/arrow-datafusion-python/pull/285) (jdye64)
- Expand Rust return type support for Arrow DataTypes in ScalarValue [#287](https://github.com/apache/arrow-datafusion-python/pull/287) (jdye64)

## [0.8.0](https://github.com/apache/arrow-datafusion-python/tree/0.8.0) (2023-02-22)

[Full Changelog](https://github.com/apache/arrow-datafusion-python/compare/0.8.0-rc1...0.8.0)

**Implemented enhancements:**

- Add support for cuDF physical execution engine [\#202](https://github.com/apache/arrow-datafusion-python/issues/202)
- Make it easier to create a Pandas dataframe from DataFusion query results [\#139](https://github.com/apache/arrow-datafusion-python/issues/139)

**Fixed bugs:**

- Build error: could not compile `thiserror` due to 2 previous errors [\#69](https://github.com/apache/arrow-datafusion-python/issues/69)

**Closed issues:**

- Integrate with the new `object_store` crate [\#22](https://github.com/apache/arrow-datafusion-python/issues/22)

**Merged pull requests:**

- Update README in preparation for 0.8 release [\#206](https://github.com/apache/arrow-datafusion-python/pull/206) ([andygrove](https://github.com/andygrove))
- Add support for cudf as a physical execution engine [\#205](https://github.com/apache/arrow-datafusion-python/pull/205) ([jdye64](https://github.com/jdye64))
- Run `maturin develop` instead of `cargo build` in verification script [\#200](https://github.com/apache/arrow-datafusion-python/pull/200) ([andygrove](https://github.com/andygrove))
- Add tests for recently added functionality [\#199](https://github.com/apache/arrow-datafusion-python/pull/199) ([andygrove](https://github.com/andygrove))
- Implement `to_pandas()` [\#197](https://github.com/apache/arrow-datafusion-python/pull/197) ([simicd](https://github.com/simicd))
- Add Python wrapper for LogicalPlan::Sort [\#196](https://github.com/apache/arrow-datafusion-python/pull/196) ([andygrove](https://github.com/andygrove))
- Add Python wrapper for LogicalPlan::Aggregate [\#195](https://github.com/apache/arrow-datafusion-python/pull/195) ([andygrove](https://github.com/andygrove))
- Add Python wrapper for LogicalPlan::Limit [\#193](https://github.com/apache/arrow-datafusion-python/pull/193) ([andygrove](https://github.com/andygrove))
- Add Python wrapper for LogicalPlan::Filter [\#192](https://github.com/apache/arrow-datafusion-python/pull/192) ([andygrove](https://github.com/andygrove))
- Add experimental support for executing SQL with Polars and Pandas [\#190](https://github.com/apache/arrow-datafusion-python/pull/190) ([andygrove](https://github.com/andygrove))
- Update changelog for 0.8 release [\#188](https://github.com/apache/arrow-datafusion-python/pull/188) ([andygrove](https://github.com/andygrove))
- Add ability to execute ExecutionPlan and get a stream of RecordBatch [\#186](https://github.com/apache/arrow-datafusion-python/pull/186) ([andygrove](https://github.com/andygrove))
- Dffield bindings [\#185](https://github.com/apache/arrow-datafusion-python/pull/185) ([jdye64](https://github.com/jdye64))
- Add bindings for DFSchema [\#183](https://github.com/apache/arrow-datafusion-python/pull/183) ([jdye64](https://github.com/jdye64))
- test: Window functions [\#182](https://github.com/apache/arrow-datafusion-python/pull/182) ([simicd](https://github.com/simicd))
- Add bindings for Projection [\#180](https://github.com/apache/arrow-datafusion-python/pull/180) ([jdye64](https://github.com/jdye64))
- Table scan bindings [\#178](https://github.com/apache/arrow-datafusion-python/pull/178) ([jdye64](https://github.com/jdye64))
- Make session configurable [\#176](https://github.com/apache/arrow-datafusion-python/pull/176) ([andygrove](https://github.com/andygrove))
- Upgrade to DataFusion 18.0.0 [\#175](https://github.com/apache/arrow-datafusion-python/pull/175) ([andygrove](https://github.com/andygrove))
- Use latest DataFusion rev in preparation for DF 18 release [\#174](https://github.com/apache/arrow-datafusion-python/pull/174) ([andygrove](https://github.com/andygrove))
- Arrow type bindings [\#173](https://github.com/apache/arrow-datafusion-python/pull/173) ([jdye64](https://github.com/jdye64))
- Pyo3 bump [\#171](https://github.com/apache/arrow-datafusion-python/pull/171) ([jdye64](https://github.com/jdye64))
- feature: Add additional aggregation functions [\#170](https://github.com/apache/arrow-datafusion-python/pull/170) ([simicd](https://github.com/simicd))
- Make from\_substrait\_plan return DataFrame instead of LogicalPlan [\#164](https://github.com/apache/arrow-datafusion-python/pull/164) ([andygrove](https://github.com/andygrove))
- feature: Implement count method [\#163](https://github.com/apache/arrow-datafusion-python/pull/163) ([simicd](https://github.com/simicd))
- CI Fixes [\#162](https://github.com/apache/arrow-datafusion-python/pull/162) ([jdye64](https://github.com/jdye64))
- Upgrade to DataFusion 17 [\#160](https://github.com/apache/arrow-datafusion-python/pull/160) ([andygrove](https://github.com/andygrove))
- feature: Improve string representation of datafusion classes [\#159](https://github.com/apache/arrow-datafusion-python/pull/159) ([simicd](https://github.com/simicd))
- Make PyExecutionPlan.plan public [\#156](https://github.com/apache/arrow-datafusion-python/pull/156) ([andygrove](https://github.com/andygrove))
- Expose methods on logical and execution plans [\#155](https://github.com/apache/arrow-datafusion-python/pull/155) ([andygrove](https://github.com/andygrove))
- Fix clippy for new Rust version [\#154](https://github.com/apache/arrow-datafusion-python/pull/154) ([andygrove](https://github.com/andygrove))
- Add DataFrame methods for accessing plans [\#153](https://github.com/apache/arrow-datafusion-python/pull/153) ([andygrove](https://github.com/andygrove))
- Use DataFusion rev 5238e8c97f998b4d2cb9fab85fb182f325a1a7fb [\#150](https://github.com/apache/arrow-datafusion-python/pull/150) ([andygrove](https://github.com/andygrove))
- build\(deps\): bump async-trait from 0.1.61 to 0.1.62 [\#148](https://github.com/apache/arrow-datafusion-python/pull/148) ([dependabot[bot]](https://github.com/apps/dependabot))
- Rename default branch from master to main [\#147](https://github.com/apache/arrow-datafusion-python/pull/147) ([andygrove](https://github.com/andygrove))
- Substrait bindings [\#145](https://github.com/apache/arrow-datafusion-python/pull/145) ([jdye64](https://github.com/jdye64))
- build\(deps\): bump uuid from 0.8.2 to 1.2.2 [\#143](https://github.com/apache/arrow-datafusion-python/pull/143) ([dependabot[bot]](https://github.com/apps/dependabot))
- Prepare for 0.8.0 release [\#141](https://github.com/apache/arrow-datafusion-python/pull/141) ([andygrove](https://github.com/andygrove))
- Improve README and add more examples [\#137](https://github.com/apache/arrow-datafusion-python/pull/137) ([andygrove](https://github.com/andygrove))
- test: Expand tests for built-in functions [\#129](https://github.com/apache/arrow-datafusion-python/pull/129) ([simicd](https://github.com/simicd))
- build\(deps\): bump object\_store from 0.5.2 to 0.5.3 [\#126](https://github.com/apache/arrow-datafusion-python/pull/126) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump mimalloc from 0.1.32 to 0.1.34 [\#125](https://github.com/apache/arrow-datafusion-python/pull/125) ([dependabot[bot]](https://github.com/apps/dependabot))
- Introduce conda directory containing datafusion-dev.yaml conda enviro… [\#124](https://github.com/apache/arrow-datafusion-python/pull/124) ([jdye64](https://github.com/jdye64))
- build\(deps\): bump bzip2 from 0.4.3 to 0.4.4 [\#121](https://github.com/apache/arrow-datafusion-python/pull/121) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump tokio from 1.23.0 to 1.24.1 [\#119](https://github.com/apache/arrow-datafusion-python/pull/119) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump async-trait from 0.1.60 to 0.1.61 [\#118](https://github.com/apache/arrow-datafusion-python/pull/118) ([dependabot[bot]](https://github.com/apps/dependabot))
- Upgrade to DataFusion 16.0.0 [\#115](https://github.com/apache/arrow-datafusion-python/pull/115) ([andygrove](https://github.com/andygrove))
- Bump async-trait from 0.1.57 to 0.1.60 [\#114](https://github.com/apache/arrow-datafusion-python/pull/114) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump object\_store from 0.5.1 to 0.5.2 [\#112](https://github.com/apache/arrow-datafusion-python/pull/112) ([dependabot[bot]](https://github.com/apps/dependabot))
- Bump tokio from 1.21.2 to 1.23.0 [\#109](https://github.com/apache/arrow-datafusion-python/pull/109) ([dependabot[bot]](https://github.com/apps/dependabot))
- Add entries for publishing production \(asf-site\) and staging docs [\#107](https://github.com/apache/arrow-datafusion-python/pull/107) ([martin-g](https://github.com/martin-g))
- Add a workflow that builds the docs and deploys them at staged or production [\#104](https://github.com/apache/arrow-datafusion-python/pull/104) ([martin-g](https://github.com/martin-g))
- Upgrade to DataFusion 15.0.0 [\#103](https://github.com/apache/arrow-datafusion-python/pull/103) ([andygrove](https://github.com/andygrove))
- build\(deps\): bump futures from 0.3.24 to 0.3.25 [\#102](https://github.com/apache/arrow-datafusion-python/pull/102) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump pyo3 from 0.17.2 to 0.17.3 [\#101](https://github.com/apache/arrow-datafusion-python/pull/101) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump mimalloc from 0.1.30 to 0.1.32 [\#98](https://github.com/apache/arrow-datafusion-python/pull/98) ([dependabot[bot]](https://github.com/apps/dependabot))
- build\(deps\): bump rand from 0.7.3 to 0.8.5 [\#97](https://github.com/apache/arrow-datafusion-python/pull/97) ([dependabot[bot]](https://github.com/apps/dependabot))
- Fix GitHub actions warnings [\#95](https://github.com/apache/arrow-datafusion-python/pull/95) ([martin-g](https://github.com/martin-g))
- Fixes \#81 - Add CI workflow for source distribution [\#93](https://github.com/apache/arrow-datafusion-python/pull/93) ([martin-g](https://github.com/martin-g))
- post-release updates [\#91](https://github.com/apache/arrow-datafusion-python/pull/91) ([andygrove](https://github.com/andygrove))
- Build for manylinux 2014 [\#88](https://github.com/apache/arrow-datafusion-python/pull/88) ([martin-g](https://github.com/martin-g))
- update release readme tag [\#86](https://github.com/apache/arrow-datafusion-python/pull/86) ([Jimexist](https://github.com/Jimexist))
- Upgrade Maturin to 0.14.2 [\#85](https://github.com/apache/arrow-datafusion-python/pull/85) ([martin-g](https://github.com/martin-g))
- Update release instructions [\#83](https://github.com/apache/arrow-datafusion-python/pull/83) ([andygrove](https://github.com/andygrove))
- \[Functions\] - Add python function binding to `functions` [\#73](https://github.com/apache/arrow-datafusion-python/pull/73) ([francis-du](https://github.com/francis-du))

## [0.8.0-rc1](https://github.com/apache/arrow-datafusion-python/tree/0.8.0-rc1) (2023-02-17)

[Full Changelog](https://github.com/apache/arrow-datafusion-python/compare/0.7.0-rc2...0.8.0-rc1)

**Implemented enhancements:**

- Add bindings for datafusion\_common::DFField [\#184](https://github.com/apache/arrow-datafusion-python/issues/184)
- Add bindings for DFSchema/DFSchemaRef [\#181](https://github.com/apache/arrow-datafusion-python/issues/181)
- Add bindings for datafusion\_expr Projection [\#179](https://github.com/apache/arrow-datafusion-python/issues/179)
- Add bindings for `TableScan` struct from `datafusion_expr::TableScan` [\#177](https://github.com/apache/arrow-datafusion-python/issues/177)
- Add a "mapping" struct for types [\#172](https://github.com/apache/arrow-datafusion-python/issues/172)
- Improve string representation of datafusion classes \(dataframe, context, expression, ...\) [\#158](https://github.com/apache/arrow-datafusion-python/issues/158)
- Add DataFrame count method [\#151](https://github.com/apache/arrow-datafusion-python/issues/151)
- \[REQUEST\] Github Actions Improvements [\#146](https://github.com/apache/arrow-datafusion-python/issues/146)
- Change default branch name from master to main [\#144](https://github.com/apache/arrow-datafusion-python/issues/144)
- Bump pyo3 to 0.18.0 [\#140](https://github.com/apache/arrow-datafusion-python/issues/140)
- Add script for Python linting [\#134](https://github.com/apache/arrow-datafusion-python/issues/134)
- Add Python bindings for substrait module [\#132](https://github.com/apache/arrow-datafusion-python/issues/132)
- Expand unit tests for built-in functions [\#128](https://github.com/apache/arrow-datafusion-python/issues/128)
- support creating arrow-datafusion-python conda environment [\#122](https://github.com/apache/arrow-datafusion-python/issues/122)
- Build Python source distribution in GitHub workflow [\#81](https://github.com/apache/arrow-datafusion-python/issues/81)
- EPIC: Add all functions to python binding `functions` [\#72](https://github.com/apache/arrow-datafusion-python/issues/72)

**Fixed bugs:**

- Build is broken [\#161](https://github.com/apache/arrow-datafusion-python/issues/161)
- Out of memory when sorting [\#157](https://github.com/apache/arrow-datafusion-python/issues/157)
- window\_lead test appears to be non-deterministic [\#135](https://github.com/apache/arrow-datafusion-python/issues/135)
- Reading csv does not work [\#130](https://github.com/apache/arrow-datafusion-python/issues/130)
- Github actions produce a lot of warnings [\#94](https://github.com/apache/arrow-datafusion-python/issues/94)
- ASF source release tarball has wrong directory name [\#90](https://github.com/apache/arrow-datafusion-python/issues/90)
- Python Release Build failing after upgrading to maturin 14.2 [\#87](https://github.com/apache/arrow-datafusion-python/issues/87)
- Maturin build hangs on Linux ARM64 [\#84](https://github.com/apache/arrow-datafusion-python/issues/84)
- Cannot install on Mac M1 from source tarball from testpypi [\#82](https://github.com/apache/arrow-datafusion-python/issues/82)
- ImportPathMismatchError when running pytest locally [\#77](https://github.com/apache/arrow-datafusion-python/issues/77)

**Closed issues:**

- Publish documentation for Python bindings [\#39](https://github.com/apache/arrow-datafusion-python/issues/39)
- Add Python binding for `approx_median` [\#32](https://github.com/apache/arrow-datafusion-python/issues/32)
- Release version 0.7.0 [\#7](https://github.com/apache/arrow-datafusion-python/issues/7)

## [0.7.0-rc2](https://github.com/apache/arrow-datafusion-python/tree/0.7.0-rc2) (2022-11-26)

[Full Changelog](https://github.com/apache/arrow-datafusion-python/compare/0.7.0...0.7.0-rc2)


## [Unreleased](https://github.com/datafusion-contrib/datafusion-python/tree/HEAD)

[Full Changelog](https://github.com/datafusion-contrib/datafusion-python/compare/0.5.1...HEAD)

**Merged pull requests:**

- use \_\_getitem\_\_ for df column selection [\#41](https://github.com/datafusion-contrib/datafusion-python/pull/41) ([Jimexist](https://github.com/Jimexist))
- fix demo in readme [\#40](https://github.com/datafusion-contrib/datafusion-python/pull/40) ([Jimexist](https://github.com/Jimexist))
- Implement select_columns [\#39](https://github.com/datafusion-contrib/datafusion-python/pull/39) ([andygrove](https://github.com/andygrove))
- update readme and changelog [\#38](https://github.com/datafusion-contrib/datafusion-python/pull/38) ([Jimexist](https://github.com/Jimexist))
- Add PyDataFrame.explain [\#36](https://github.com/datafusion-contrib/datafusion-python/pull/36) ([andygrove](https://github.com/andygrove))
- Release 0.5.0 [\#34](https://github.com/datafusion-contrib/datafusion-python/pull/34) ([Jimexist](https://github.com/Jimexist))
- disable nightly in workflow [\#33](https://github.com/datafusion-contrib/datafusion-python/pull/33) ([Jimexist](https://github.com/Jimexist))
- update requirements to 37 and 310, update readme [\#32](https://github.com/datafusion-contrib/datafusion-python/pull/32) ([Jimexist](https://github.com/Jimexist))
- Add custom global allocator [\#30](https://github.com/datafusion-contrib/datafusion-python/pull/30) ([matthewmturner](https://github.com/matthewmturner))
- Remove pandas dependency [\#25](https://github.com/datafusion-contrib/datafusion-python/pull/25) ([matthewmturner](https://github.com/matthewmturner))
- upgrade datafusion and pyo3 [\#20](https://github.com/datafusion-contrib/datafusion-python/pull/20) ([Jimexist](https://github.com/Jimexist))
- update maturin 0.12+ [\#17](https://github.com/datafusion-contrib/datafusion-python/pull/17) ([Jimexist](https://github.com/Jimexist))
- Update README.md [\#16](https://github.com/datafusion-contrib/datafusion-python/pull/16) ([Jimexist](https://github.com/Jimexist))
- apply cargo clippy --fix [\#15](https://github.com/datafusion-contrib/datafusion-python/pull/15) ([Jimexist](https://github.com/Jimexist))
- update test workflow to include rust clippy and check [\#14](https://github.com/datafusion-contrib/datafusion-python/pull/14) ([Jimexist](https://github.com/Jimexist))
- use maturin 0.12.6 [\#13](https://github.com/datafusion-contrib/datafusion-python/pull/13) ([Jimexist](https://github.com/Jimexist))
- apply cargo fmt [\#12](https://github.com/datafusion-contrib/datafusion-python/pull/12) ([Jimexist](https://github.com/Jimexist))
- use stable not nightly [\#11](https://github.com/datafusion-contrib/datafusion-python/pull/11) ([Jimexist](https://github.com/Jimexist))
- ci: test against more compilers, setup clippy and fix clippy lints [\#9](https://github.com/datafusion-contrib/datafusion-python/pull/9) ([cpcloud](https://github.com/cpcloud))
- Fix use of importlib.metadata and unify requirements.txt [\#8](https://github.com/datafusion-contrib/datafusion-python/pull/8) ([cpcloud](https://github.com/cpcloud))
- Ship the Cargo.lock file in the source distribution [\#7](https://github.com/datafusion-contrib/datafusion-python/pull/7) ([cpcloud](https://github.com/cpcloud))
- add \_\_version\_\_ attribute to datafusion object [\#3](https://github.com/datafusion-contrib/datafusion-python/pull/3) ([tfeda](https://github.com/tfeda))
- fix ci by fixing directories [\#2](https://github.com/datafusion-contrib/datafusion-python/pull/2) ([Jimexist](https://github.com/Jimexist))
- setup workflow [\#1](https://github.com/datafusion-contrib/datafusion-python/pull/1) ([Jimexist](https://github.com/Jimexist))

## [0.5.1](https://github.com/datafusion-contrib/datafusion-python/tree/0.5.1) (2022-03-15)

[Full Changelog](https://github.com/datafusion-contrib/datafusion-python/compare/0.5.1-rc1...0.5.1)

## [0.5.1-rc1](https://github.com/datafusion-contrib/datafusion-python/tree/0.5.1-rc1) (2022-03-15)

[Full Changelog](https://github.com/datafusion-contrib/datafusion-python/compare/0.5.0...0.5.1-rc1)

## [0.5.0](https://github.com/datafusion-contrib/datafusion-python/tree/0.5.0) (2022-03-10)

[Full Changelog](https://github.com/datafusion-contrib/datafusion-python/compare/0.5.0-rc2...0.5.0)

## [0.5.0-rc2](https://github.com/datafusion-contrib/datafusion-python/tree/0.5.0-rc2) (2022-03-10)

[Full Changelog](https://github.com/datafusion-contrib/datafusion-python/compare/0.5.0-rc1...0.5.0-rc2)

**Closed issues:**

- Add support for Ballista [\#37](https://github.com/datafusion-contrib/datafusion-python/issues/37)
- Implement DataFrame.explain [\#35](https://github.com/datafusion-contrib/datafusion-python/issues/35)

## [0.5.0-rc1](https://github.com/datafusion-contrib/datafusion-python/tree/0.5.0-rc1) (2022-03-09)

[Full Changelog](https://github.com/datafusion-contrib/datafusion-python/compare/4c98b8e9c3c3f8e2e6a8f2d1ffcfefda344c4680...0.5.0-rc1)

**Closed issues:**

- Investigate exposing additional optimizations [\#28](https://github.com/datafusion-contrib/datafusion-python/issues/28)
- Use custom allocator in Python build [\#27](https://github.com/datafusion-contrib/datafusion-python/issues/27)
- Why is pandas a requirement? [\#24](https://github.com/datafusion-contrib/datafusion-python/issues/24)
- Unable to build [\#18](https://github.com/datafusion-contrib/datafusion-python/issues/18)
- Setup CI against multiple Python version [\#6](https://github.com/datafusion-contrib/datafusion-python/issues/6)

\* _This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)_


\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
